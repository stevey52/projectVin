from django.urls import path
from .views import HomePageView, AboutPageView, BaseViewPage

urlpatterns = [
    path("",HomePageView.as_view(), name="home"),
    path("about/",AboutPageView.as_view(), name="about"),
    path("base/",BaseViewPage.as_view(), name="base")
]
