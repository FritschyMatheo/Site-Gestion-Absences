from django.urls import path
from . import views, cours_views, enseignant_views, etu_views, grp_etudiant_views, etu_views, grp_etudiant_views

urlpatterns = [
    #views
    path('index/', views.index),


    #cours_views.py
    path('Cours/ajout', cours_views.ajout),


    #absence_views.py,



    #grp_etudiant_views
    path('Groupe/ajout', grp_etudiant_views.ajout),
    path('Groupe/traitement', grp_etudiant_views.traitement),
    path('Groupe/accueil', grp_etudiant_views.accueil),
    path('Groupe/affiche/<int:id>/', grp_etudiant_views.affiche),
    path('Groupe/update/<int:id>/', grp_etudiant_views.update),
    path('Groupe/updatetraitement/<int:id>/', grp_etudiant_views.updatetraitement),
    path('Groupe/delete/<int:id>', grp_etudiant_views.delete),

    #enseignant_views
    path('Enseignant/ajout', enseignant_views.ajout),
    path('Enseignant/traitement', enseignant_views.traitement),
    path('Enseignant/accueil', enseignant_views.accueil),
    path('Enseignant/affiche/<int:id>/', enseignant_views.affiche),
    path('Enseignant/update/<int:id>/', enseignant_views.update),
    path('Enseignant/updatetraitement/<int:id>/', enseignant_views.updatetraitement),
    path('Enseignant/delete/<int:id>', enseignant_views.delete),
]