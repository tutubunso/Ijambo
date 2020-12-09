from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_event/', views.event, name="addevent"),
    path('indexer/', views.indexe, name="indexer"),
    path('suggestion/', views.contact, name="contact"),
    path('payer/<int:id>/', views.paiement,name="paiement"),
    path('liste/',views.listevents,name="listevents"),
    path('supprimer/<int:id>/', views.delete,name="supprimerE"),
    
]
