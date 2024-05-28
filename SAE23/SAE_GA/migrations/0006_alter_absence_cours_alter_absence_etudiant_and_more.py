# Generated by Django 5.0.6 on 2024-05-28 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAE_GA', '0005_alter_etudiant_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='cours',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SAE_GA.cours'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='etudiant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SAE_GA.etudiant'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAE_GA.enseignant'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='groupe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SAE_GA.groupe'),
        ),
    ]
