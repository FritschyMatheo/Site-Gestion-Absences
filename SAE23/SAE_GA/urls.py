from django.urls import path
from . import views, cours_views, enseignant_views, etu_views, grp_etudiant_views, etu_views, grp_etudiant_views

urlpatterns = [
    #views
    path('index/', views.index),



    #grp_etudiant_views
    path('Groupe/ajout', grp_etudiant_views.ajout),
    path('Groupe/traitement', grp_etudiant_views.traitement),
    path('Groupe/accueil', grp_etudiant_views.accueil),
    path('Groupe/affiche/<int:id>/', grp_etudiant_views.affiche),
    path('Groupe/update/<int:id>/', grp_etudiant_views.update),
    path('Groupe/updatetraitement/<int:id>/', grp_etudiant_views.updatetraitement),
    path('Groupe/delete/<int:id>', grp_etudiant_views.delete),
]