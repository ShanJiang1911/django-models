from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class SnackListView(ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
