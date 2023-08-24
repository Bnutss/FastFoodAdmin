from django.urls import path
from .views import DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView

urlpatterns = [
    path('', DishListView.as_view(), name='dish-list'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('dish/add/', DishCreateView.as_view(), name='dish-add'),
    path('dish/<int:pk>/update/', DishUpdateView.as_view(), name='dish-update'),
    path('dish/<int:pk>/delete/', DishDeleteView.as_view(), name='dish-delete'),
]
