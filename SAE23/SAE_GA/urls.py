from django.urls import path
from . import views, cours_views, enseignant_views, etu_views, grp_etudiant_views, etu_views, grp_etudiant_views

urlpatterns = [
    path('index/', views.index)
]