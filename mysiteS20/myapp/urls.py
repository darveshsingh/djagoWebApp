from django.urls import path
from myapp import views
from django.conf.urls import *
app_name = "myapp"
urlpatterns = [
    path(r'', views.index, name="index"),
    path(r"about/", views.about, name="about"),
    url(r"^(?P<top_no>\w+)/$", views.detail, name="detail"),
]
