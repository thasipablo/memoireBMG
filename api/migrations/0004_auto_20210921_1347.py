# Generated by Django 3.2.7 on 2021-09-21 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_nom_enseigant_enseignant_nom_enseignant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='departement',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='departement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.departement'),
            preserve_default=False,
        ),
    ]
