from django.urls import path
import blog.views

urlpatterns = [
  path("",blog.views.index)
  path("post/<slug>/",blog.views.post_detail,name="blog-post-detail")
]