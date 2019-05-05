from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect,HttpResponseRedirect
from monAsso.models import Asso,Benevole, Event
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpAssoForm,SignUpBenevoleForm, EventForm




#Une vue=une fonction dans le fichier view.py (prend en param une requete http et renvoie une reponse http)
#chaque vue doit etre associee au minimum a une url

#page d'inscription
def signup(request,userType):
    #sign-up for association
    if userType=='asso':
        if request.method == 'POST':
            form = SignUpAssoForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                nomAsso=form.cleaned_data.get('nomAsso')
                typeAsso = form.cleaned_data.get('nomAsso')
                description = form.cleaned_data.get('description')


                user = authenticate(username=username, password=raw_password)
                login(request, user)
                #Creation d'un modele Asso
                asso=Asso(nomAsso=nomAsso,typeAsso=typeAsso,description=description,userResponsable=user)
                asso.save()
                return redirect('/profile')
        else:
            form = SignUpAssoForm()
        return render(request, 'monAsso/signup.html', {'form': form})
    #sign-up for benevole
    if userType == 'benevole':
        if request.method == 'POST':
            form = SignUpBenevoleForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                # Creation d'un modele Benevole
                benevole=Benevole(userResponsable=user)

                benevole.save()
                return redirect('profile')
        else:
            form = SignUpBenevoleForm()
        return render(request, 'monAsso/signup.html', {'form': form})

#log in page view
def signin(request):
    #gestion connexion
    return render(request,'monAsso/sign-in.html')

#log out page view
def signout(request):
    return render(request,'monAsso/sign-out.html')

#index page view: page d'accueil
def getIndex(request):
    return render(request,'monAsso/index.html')

#Event page view
def showEvent(request):
    return render(request,'monAsso/events.html')

#affichage du profil utilisateur
def showProfile(request):
    user = request.user
    try:
        #try matching user with a benevole account
        myBenevole=Benevole.objects.get(userResponsable=user)
        return render(request,'monAsso/show-benevole-profile.html',locals())
    except:
        #try matching user with association account
        myAsso=Asso.objects.get(userResponsable=user)
        return render(request,'monAsso/show-association-profile.html',locals())

#create an event
def createEvent(request):
    user=request.user
    try:
        #check is user is an association account
        myAsso=Asso.objects.get(userResponsable=user)
    except:
        return redirect('profile')
    form = EventForm(request.POST or None)
    if form.is_valid():
        nomEvent = form.cleaned_data.get('nomEvent')
        lieu = form.cleaned_data.get('lieu')
        dateDebut = form.cleaned_data.get('dateDebut')
        dateFin = form.cleaned_data.get('dateFin')
        description = form.cleaned_data.get('description')
        nbBenevole = form.cleaned_data.get('nbBenevole')
        # creation d'un evenement
        newEvent = Event(nomEvent=nomEvent, lieu=lieu, dateDebut=dateDebut, dateFin=dateFin, description=description,
                         nbBenevole=nbBenevole)
        newEvent.save()
        # a revoir: on redirige vers la page event
        return redirect('events')
    else:
        form = EventForm(request.POST or None)
    return render(request, 'monAsso/create-event.html', {'form': form})


#test
def ficheAsso(request,asso):
    monAsso=get_object_or_404(Asso,nomAsso=asso)
    return render(request,'monAsso/ficheAsso.html',{'association':monAsso})


