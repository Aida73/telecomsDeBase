from django.shortcuts import render, HttpResponse
from .models import *
from gtts import gTTS
import os
import sox
import shutil

# Create your views here.
def convertToUlaw(filename):
    print(os.path.basename)
    #lame --decode somemp3file.mp3 output.wav
    #os.system(f"sox sounds/{filename}.mp3 -r 8000 -c 1 ./sounds/{filename}.ulaw") #ici on va mettre le chemin vers sounds de astrisk
    os.system(f"lame --decode sounds/{filename}.mp3 sounds/{filename}.wav")
    os.system(f"sox -V sounds/{filename}.wav -r 8000 -c 1 -t ul sounds/{filename}.ulaw")
    os.remove(f"sounds/{filename}.wav")
    os.remove(f"sounds/{filename}.mp3")




def translate(text, language, filename):
    vocal = gTTS(text=text, lang=language, slow=False)
    vocal.save(f"./sounds/{filename}.mp3")
    convertToUlaw(filename)
    

def convertDate(date):
    listeMois = ['janvier','février','mars','avril','mai','juin','août',
            'septembre','octobre','novembre','décembre']
    mois = listeMois[date.month-1]
    converted = f"{date.day} {mois} {date.year}"
    return converted





def getEtatDossier(request,numero):
    text = ""
    try:
        candidat = Candidat.objects.get(numDossier=numero)
        if candidat.etat == 'en cours de traitement':
            text = f"Bonjour {candidat.prenom} {candidat.nom}.Les résultats du concours ne sont pas encore disponibles. Merci de patienter"
        elif candidat.etat == 'accepté':
            text = f"Bonjour {candidat.prenom} {candidat.nom}.Félicitation à vous Votre dossier est {candidat.etat}."
        elif candidat.etat == 'rejeté':
            text = f"Bonjour {candidat.prenom} {candidat.nom}.Nous sommes desolés mais vous n'avez pas réussi au concours. Merci d'avoir participé"
        else :
            text = f"Bonjour {candidat.prenom} {candidat.nom}.Vous êtes admis sur la liste d'attente. Rester à l'écoute, on vous reviendra bientot"

    except Candidat.DoesNotExist:
        text = "Désolé votre dossier n'existe pas"

    translate(text,'fr','dossier')
    return HttpResponse(text)



def getDateConcours(request):
    text = ""
    try:
        session = Session.objects.get(id=1)
        print("date ",convertDate(session.dateConcours))
        text= f"Le concours de cette année se tiendra le {convertDate(session.dateConcours)}.\nN'oubliez pas de Présenter une pièce d'identité en cours de validité le jour du concours, ou une carte d'identité scolaire valide."
    except:
        text = "Une date n'a pas encore été retenue. Veuillez nous recontacter plutard"
        print("date ",convertDate(session.dateConcours))

    translate(text,'fr','dateConcours')
    return HttpResponse(text)



def getDateDepotConcours(request):
    text = ""
    try:
        session = Session.objects.get(id=1)
        text= f"Vous pourrez déposer vos dossiers à partir du {convertDate(session.date_ouverture_depot)}"
    except:
        text = "Une date n'a pas encore été retenue. Veuillez nous recontacter plutard"

    translate(text,'fr','dateDepotConcours')
    return HttpResponse(text)




def getDateDepotReleves(request):
    text = ""
    try:
        session = Session.objects.get(id=1)
        text= f"si vous réussi au baccalauréat, veuillez déposer vos relevés de notes au plutard le {convertDate(session.date_depot_releves)}"
    except:
        text = "Une date n'a pas encore été retenue. Veuillez nous recontacter plutard"

    translate(text,'fr','dateDepotReleves')
    return HttpResponse(text)



def getDateLimiteDepots(request):
    text=""
    try:
        session = Session.objects.get(id=1)
        text= f"La date limite des depots est le {convertDate(session.date_limite_depot)}"
    except:
        text = "Une date n'a pas encore été retenue. Veuillez nous recontacter plutard"

    translate(text,'fr','dateLimiteDepotConcours')
    return HttpResponse(text)


def getFilieres(request):
    text="les différents candidats suivront une formation de cinquant : \n deuzan de tronc commun et troizan de spécialisation dans les filières suivantes:\n"
    try:
        filieres = Filiere.objects.all()
        index=1
       
        for filiere in filieres:
            print(index)
            print(filiere)
            text+=f"{str(index)} \n {filiere}\n"
            index+=1 

    except:
        text = "erreur de saisie"


    translate(text,'fr','filieres')
    return HttpResponse(text)


