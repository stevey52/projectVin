from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class BaseViewPage(TemplateView):
    template_name = "bw.html"

class OutdoorPageView(TemplateView):
    template_name = "outdoor.html"
