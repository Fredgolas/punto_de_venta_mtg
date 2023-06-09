from django.urls import path, re_path
#from productos.views import CardListInventory, CardCreateView, CardDeleteView, CardUpdateView
#from django.conf.urls import url
from productos.views import home, card_collection, cart_checkup

urlpatterns = [
    # path('inventario/', CardListInventory.as_view()),
    # path('inventario/nueva-carta', CardCreateView.as_view()),
    # path('inventario/modificar/<int:pk>', CardUpdateView.as_view()),
    # path('inventario/eliminar/<int:pk>', CardDeleteView.as_view()),
    re_path(r'^$', home),
    
    re_path(r'^api/cards/$', card_collection),
    re_path(r'^api/cart/(?P<pk>[0-9]+)$', cart_checkup)
    #re_path(r'^api/cards/(?P<pk>[0-9]+)$', ''),
]