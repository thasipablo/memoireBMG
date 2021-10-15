from django.http import HttpResponseRedirect, HttpResponse, response
import csv

from api.models import Etudiant


def create_csv(course_name, departement, promotion):

    file = open(f'cotes/{course_name}.csv', 'w')

    writer = csv.writer(file)
    
    etudiants = Etudiant.objects.all()

    writer.writerow(['Matricules', 'TP', 'TD', 'Intérogation', 'Examen', 'Total'])
    
    for etudiant in etudiants:
        writer.writerow([etudiant.matricule])

    print(file)

    
    return file.name
