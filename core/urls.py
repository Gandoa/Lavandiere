from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='accueil'),
    path('commande', views.commande, name='commande'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('be_partners/', views.be_partners, name='be_partners'),
    path('pressing/', views.pressing, name='pressing'),
      path('gallery/', views.gallery, name='gallery'),
]