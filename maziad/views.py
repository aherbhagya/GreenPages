from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext


class HomePage(TemplateView):
    template_name = 'maziad/index.html'
    # model = Category

# def get_context_data(self, **kwargs):
#     # context = super(Guitardetails, self).get_context_data(**kwargs)
#     context['guitar'] = Category.objects.all()
#     return context

class ServiceProviderListView(ListView):
    template_name = 'maziad/serviceprovider.html'
    model = ServiceProvider

    def get_context_data(self, **kwargs):
        context = super(ServiceProviderListView, self).get_context_data(**kwargs)
        context['serviceprovider'] = ServiceProvider.objects.all()
        return context

class ServiceProviderDetailView(DetailView):
    model = ServiceProvider
  #  template_name = 'guitar/serviceprovider_detail.html'

