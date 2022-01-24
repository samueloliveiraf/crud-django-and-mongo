from django.shortcuts import render
from django.views.generic import (
    CreateView, 
    ListView,
    DeleteView, 
    UpdateView,
)
from django.urls import reverse_lazy

from .models import Product


def home(request):
   
    return render(request, 'index.html')


class ListViewProduct(ListView):
    template_name = 'index.html'
    model = Product

    
    def get_queryset(self):
        queryset = super(ListViewProduct, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CrieteViewProduct(CreateView):
    template_name = 'products/create_product.html'
    model = Product

    fields = [
        'name',
        'image'
    ]
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  
    
    success_url = reverse_lazy('home')


class UpadateViewProduct(UpdateView):
    template_name = 'products/update_product.html'
    model = Product

    fields = [
        'name',
        'image'
    ]

    success_url = reverse_lazy('home')


class DeleteViewProduct(DeleteView):
    template_name = 'products/delete_product.html'
    model = Product

    success_url = reverse_lazy('home')
