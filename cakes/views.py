from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Cakes


class Home(ListView):
    template_name = 'cakes/home.html'
    model = Cakes
    paginate_by = 6
