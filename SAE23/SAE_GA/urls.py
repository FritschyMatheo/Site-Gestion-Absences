from django.urls import path
from . import views, cours_views, enseignant_views, grp_etudiant_views, etu_views, grp_etudiant_views, absence_views

urlpatterns = [
    #views
    path('index/', views.index),


    #absence_views
    path('Absence/ajout', absence_views.ajout),
    path('Absence/traitement', absence_views.traitement),
    path('Absence/accueil', absence_views.accueil),
    path('Absence/affiche/<int:id>/', absence_views.affiche),
    path('Absence/update/<int:id>/', absence_views.update),
    path('Absence/updatetraitement/<int:id>/', absence_views.updatetraitement),
    path('Absence/delete/<int:id>', absence_views.delete),

    #cours_views
    path('Cours/ajout', cours_views.ajout),
    path('Cours/traitement', cours_views.traitement),
    path('Cours/accueil', cours_views.accueil),
    path('Cours/affiche/<int:id>/', cours_views.affiche),
    path('Cours/update/<int:id>/', cours_views.update),
    path('Cours/updatetraitement/<int:id>/', cours_views.updatetraitement),
    path('Cours/delete/<int:id>', cours_views.delete),

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

    #etudiant_views
    path('Etudiant/ajout', etu_views.ajout),
    path('Etudiant/traitement', etu_views.traitement),
    path('Etudiant/accueil', etu_views.accueil),
    path('Etudiant/affiche/<int:id>/', etu_views.affiche),
    path('Etudiant/update/<int:id>/', etu_views.update),
    path('Etudiant/updatetraitement/<int:id>/', etu_views.updatetraitement),
    path('Etudiant/delete/<int:id>', etu_views.delete)
]