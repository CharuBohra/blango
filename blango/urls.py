"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path ,include
import blog.views 
from django.conf import settings
import blango_auth.views

from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
#from blango.views import test_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",blog.views.index),
    # path("test-cache/", blog.views.test_cache),
    path("ip/", blog.views.get_ip),
    path("post/<slug>/",blog.views.post_detail , name="blog-post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path(
      "accounts/register/",
      RegistrationView.as_view(form_class=BlangoRegistrationForm),
      name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("blog.api.urls")),
]
print(f"Time Zone:{settings.TIME_ZONE}")
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/",include(debug_toolbar.urls)),
    ]

