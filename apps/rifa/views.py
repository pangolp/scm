from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from .forms import PersonaForm, UserForm

@login_required
def rifa_personas_ver(request):
	personas = Persona.objects.all()
	return render(request, 'rifa/personas/personas.html', {'personas': personas})

@login_required
def rifa_personas_agregar(request):
	if request.method == 'POST':
		formulario = PersonaForm(request.POST)
		formulario2 = UserForm(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			return HttpResponseRedirect(reverse_lazy('core_perfil'))
	else:
		formulario = PersonaForm()
		formulario2 = UserForm()
	return render(request, 'rifa/personas/agregar.html', {'formulario': formulario, 'formulario2': formulario2})