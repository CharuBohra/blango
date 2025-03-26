from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
import logging
from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache
from django.utils.cache import get_cache_key

logger = logging.getLogger(__name__)

# from django.core.cache import cache
# from django.http import HttpResponse

# def test_cache(request):
#     if cache.get("cache_test"):
#         return HttpResponse("✅ Serving from cache!")

#     cache.set("cache_test", "Cache is now working!", timeout=60)
#     return HttpResponse("❌ First request, caching now!")

# @cache_page(120, key_prefix="index_page")
def index(request):
    # logger.debug("Index function is called!")

    # cache_key = f"index_page_cache"
    # logger.debug(f"Cache Key: {cache_key}")

    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))

    return render(request, "blog/index.html", {"posts": posts})


# def index(request):
#     cached_page = cache.get("index_page")
#     if cached_page:
#         print("✅ Serving from cache!")
#         return HttpResponse(cached_page)

#     print("❌ Caching new response!")
#     response = "<h1>Hello, this is cached!</h1>"
#     cache.set("index_page", response, timeout=300)  # Cache for 5 minutes
#     return HttpResponse(response)
def post_detail(request,slug):
  post = get_object_or_404(Post, slug=slug)
  comment_form = None
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.content_object = post
          comment.creator = request.user
          comment.save()
          return redirect(request.path_info)
    else:
      comment_form = CommentForm()
  else:
      comment_form = None
  logger.info("Created comment on Post %d for user %s", post.pk, request.user)
  print("DEBUG: Comment form:", comment_form)  # Debugging output
  return render(request,"blog/post-detail.html" , {"post":post , "comment_form":comment_form})

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])