from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from ijambo.models import *
from .forms import *
# Create your views here.

def home(request):
	try:
		profile = Profil.objects.get(user=request.user)
		return render(request, 'simple_user.html', locals())
	except Exception as e:
		err_msg = "You must login first to access this page !"
		return render(request, '404.html', locals())
	

def event(request):
	events_form = eventsForm(request.POST or None, request.FILES)
	if(request.method == 'POST'):
		if(events_form.is_valid()):
			events_form.save()
			return redirect('listevents')
	events_form = eventsForm()
	return render(request, "forms.html", locals())

def contact(request):
	contact_form = contactForm(request.POST or None)
	if (request.method == 'POST'):
		if(contact_form.is_valid()):
			contact_form.save()

	contact_form = contactForm()

	return render(request, "forms.html", locals())




def paiement(request, id):
	text1="via lumicash" 
	number="68235685"
	text2="via ecocash" 
	number2="72456078"
	event = events.objects.get(id=id)
	paiement_form=paiementForm(request.POST or None)
	if(request.method == 'POST'):
		if(paiement_form.is_valid()):

			paiement_form.save()
			event.paid=True
			event.save()

	paiement_form=paiementForm()
	return render(request,"forms.html",locals())


def listevents(request):
	listes = events.objects.all()
	return render(request,"listevents.html", locals())

def delete(request,id):
	event= events.objects.get(id=id)
	event.delete()
	return redirect(listevents)

def indexe(request):
	text = "Bonjour le monde, Bienvenue sur notre site Web"
	text2 = "Aymar membres du crew"
	nummber = 42510

	return render(request, "indexe.html", locals())
	


