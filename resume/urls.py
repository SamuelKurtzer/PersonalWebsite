from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
        path('', views.index, name="index"),
] + static('/file', document_root='pdf/ResumeSamuelKurtzer201904.pdf')

