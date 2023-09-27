from django.shortcuts import render, redirect
from .forms import CommandeForm, ContactForm
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            Nom = form.cleaned_data['Nom']
            Numéro_de_Téléphone = form.cleaned_data['Numéro_de_Téléphone']
            Email = form.cleaned_data['Email']
            Services = form.cleaned_data['Services']
            Code = form.cleaned_data['Code']
            Commentaire = form.cleaned_data['Commentaire']
            commande = CommandeModel.objects.create(Nom=Nom, Numéro_de_Téléphone=Numéro_de_Téléphone,Email=Email,Services=Services,Code=Code,Commentaire=Commentaire)
            if commande is not None:
                commande.save()
                messages.success(request, "Demande a bien été réceptionné ! Nous vous contacterons sous peu")
                return redirect('accueil')
            else:
                messages.error(request, "Impossible de soummettre votre demande, veuillez bien renseigner les champs")
                return redirect('commande')

    else:
        context ={}
        context['form']= CommandeForm()
        return render(request, 'commande.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            numéro = form.cleaned_data['numéro']
            Email = form.cleaned_data['Email']
            Message = form.cleaned_data['Message']
            new_contact = ContactModel.objects.create(nom=nom, numéro=numéro,Email=Email,Message=Message)
            if new_contact is not None:
                new_contact.save()
                messages.success(request, "Demande a bien été réceptionné ! Nous vous contacterons sous peu")
                return redirect('accueil')
            else:
                messages.error(request, "Impossible de soummettre votre demande, veuillez bien renseigner les champs")
                return redirect('contact')

    else: 
        context ={}
        context['form']= ContactForm()
        return render(request, 'contact.html',context )

def partners(request):
    return render(request, 'partners.html')

def be_partners(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        name_enterprise = request.POST['name_enterprise']
        domain = request.POST['domain']
        new_partner = Partner(first_name=first_name,last_name=last_name,email=email,city=city,name_enterprise=name_enterprise,domain=domain)
        if new_partner is not None:
            new_partner.save()
            messages.success(request, "Demande a bien été réceptionné ! Nous vous contacterons sous peu")
            return redirect('accueil')
        else:
            messages.error(request, "Impossible de soummettre votre demande, veuillez bien renseigner les champs")
            return redirect('be_partners')

    else:
        return render(request, 'be_partners.html')

def about(request):
    return render(request, 'about.html')

def pressing(request):
    return render(request, 'pressing.html')

def gallery(request):
    return render(request, 'gallery.html')
