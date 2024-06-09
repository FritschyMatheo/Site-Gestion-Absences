# Site-Gestion-Absences
Dossier collaboratif pour le projet d'une application web

Lien d'accès à l'application une fois lancée : http://127.0.0.1:8000/SAE_GA/index/
Lien vers le diagramme de Gantt : https://docs.google.com/spreadsheets/d/1d6RenvtC3c0h3syrMU_4JIkwq9jAMNIQzPLKsjbCpBk/edit#gid=0

Schéma de données du site à respecter dans la base de donnée "db_django_sae23": 

    Groupes d'Étudiants
        id
        nom

    Étudiants
        id
        nom
        prenom
        email
        groupe (relation avec Groupes d'Étudiants)
        photo

    Enseignants
        id
        nom
        prenom
        email

    Cours
        id
        titre
        date
        enseignant (relation avec Enseignants)
        duree
        groupe (relation avec Groupes d'Étudiants)

    Absences
        etudiant (relation avec Étudiants)
        cours (relation avec Cours)
        justifie (boolean)
        justification (texte)

    Relations entre les Modèles :

    -Un Groupe d'Étudiants a plusieurs Étudiants.
    -Un Enseignant peut enseigner plusieurs Cours.
    -Un Groupe d'Étudiants peut assister à plusieurs Cours.
    -Une Absence est associée à un Étudiant et à un Cours.
