from django.db import models

# Create your models here.

class Centre(models.Model):
    nom = models.CharField(max_length=50) 
    adresse = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Centre")
        verbose_name_plural = ("Centres")

    def __str__(self):
        return self.nom

  
class Candidat(models.Model):

    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    numDossier = models.CharField(max_length=50)
    date_depot = models.DateTimeField(auto_now_add=True)
    INPROCESS = 'en cours de traitement'
    ACCEPTED = 'accepté'
    REJECTED = 'rejeté'
    WAITING = "sur la liste d'attente"
    ETAT_CHOICES = (
        (INPROCESS,INPROCESS),
        (ACCEPTED,ACCEPTED),
        (REJECTED,REJECTED),
        (WAITING,WAITING),
    )
    etat = models.CharField(max_length=22,choices=ETAT_CHOICES, default=WAITING)
    centre_examen = models.ForeignKey(Centre, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Candidat")
        verbose_name_plural = ("Candidats")

    def __str__(self):
        return self.numDossier


class Session(models.Model):
    annee = models.CharField(max_length=50)
    dateConcours = models.DateField()
    date_ouverture_depot = models.DateField()
    date_limite_depot = models.DateField()
    date_depot_releves = models.DateField(blank=True,null=True)
    class Meta:
        verbose_name = ("Session")
        verbose_name_plural = ("Sessions")

    def __str__(self):
        return str(self.dateConcours)



