# Generated by Django 3.2.7 on 2021-09-21 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_nom_course_cours_nom_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.enseignant'),
        ),
        migrations.RemoveField(
            model_name='cours',
            name='promotion',
        ),
        migrations.AddField(
            model_name='cours',
            name='promotion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.promotion'),
            preserve_default=False,
        ),
    ]
