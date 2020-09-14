from django.urls import path, re_path
from django.conf.urls import url
#from . import views
from .views import blogList, blogPost

urlpatterns = [
        path('', blogList.as_view(), name="blogList"),
        re_path(r'^post/(?P<pk>\d+)/$', blogPost.as_view(), name='blogPost')
]
