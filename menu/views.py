from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Dish


class DishListView(ListView):
    model = Dish
    template_name = 'menu/dish_list.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'menu/dish_detail.html'
    context_object_name = 'dish'


class DishCreateView(CreateView):
    model = Dish
    template_name = 'menu/dish_form.html'
    fields = ['name', 'category', 'description', 'price']
    success_url = reverse_lazy('dish-list')


class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'menu/dish_update.html'
    fields = ['name', 'category', 'description', 'price']
    success_url = reverse_lazy('dish-list')


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy('dish-list')
