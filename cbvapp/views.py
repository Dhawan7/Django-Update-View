from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                DetailView, CreateView,UpdateView)
from .models import Collage,student

class MyCBV(TemplateView):
    template_name= 'index.html'

class collageList(ListView):
    context_object_name = 'collages_list'
    model = Collage

class collageDetail(DetailView):
    context_object_name = 'detail'
    model= Collage
    template_name = 'cbvapp/collage_detail.html'

class CollageCreateView(CreateView):
    fields = ('name','principal_name','location','contact_no')
    model = Collage

class CollageUpdateView(UpdateView):
    fields = ('name','principal_name','contact_no')
    model = Collage
