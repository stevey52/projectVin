from django.urls import path
from .views import HomePageView,AboutPageView,BaseViewPage
from .views import OutdoorPageView,IndoorPageView,ProductsView

urlpatterns = [
    path("",HomePageView.as_view(), name="home"),
    path("about/",AboutPageView.as_view(), name="about"),
    path("b&w/",BaseViewPage.as_view(), name="bw"),
    path("outdoor/",OutdoorPageView.as_view(), name="outdoor"),
    path("indoor/",IndoorPageView.as_view(), name="indoor"),
    path("products/",ProductsView.as_view(), name="products")
]
