from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'
class AboutPageView(TemplateView):
    template_name = 'app/about.html'  
class ServicesPageView(TemplateView):
    template_name = 'app/services.html' 
class ContactPageView(TemplateView):
    template_name = 'app/contact.html' 
class AlbumPageView(TemplateView):
    template_name = 'app/album.html' 
  