from django.urls import path
#from . import views
from .views import blogList

urlpatterns = [
        path('', blogList.as_view(), name="blog")
]
