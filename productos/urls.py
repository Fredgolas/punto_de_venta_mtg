from django.urls import path
from productos.views import CardListInventory, CardCreateView, CardDeleteView, CardUpdateView


urlpatterns = [
    path('inventario/', CardListInventory.as_view()),
    path('inventario/nueva-carta', CardCreateView.as_view()),
    path('inventario/modificar/<int:pk>', CardUpdateView.as_view()),
    path('inventario/eliminar/<int:pk>', CardDeleteView.as_view()),
]