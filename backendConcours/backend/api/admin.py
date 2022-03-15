from django.contrib import admin
from api.models import *


@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','numDossier','date_depot','etat','centre_examen')

@admin.register(Centre)
class CentreAdmin(admin.ModelAdmin):
    list_display = ('nom','adresse')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('annee','dateConcours','date_ouverture_depot','date_limite_depot','date_depot_releves')

