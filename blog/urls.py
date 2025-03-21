from django.urls import path
import blog.views

urlpatterns = [
  path("",blog.views.index)
]