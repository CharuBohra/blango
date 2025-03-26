from django.urls import path
import blog.views
# from .views import test_cache

urlpatterns = [
  path("",blog.views.index)
  path("post/<slug>/",blog.views.post_detail,name="blog-post-detail")
]