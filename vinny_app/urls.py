from django.urls import path
from .views import HomePageView,AboutPageView,BaseViewPage,OutdoorPageView

urlpatterns = [
    path("",HomePageView.as_view(), name="home"),
    path("about/",AboutPageView.as_view(), name="about"),
    path("b&w/",BaseViewPage.as_view(), name="bw"),
    path("outdoor/",OutdoorPageView.as_view(), name="outdoor")
]
