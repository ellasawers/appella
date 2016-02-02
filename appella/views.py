from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Usuario
from .forms import FormaRegistro

def registrar(request):
	if request.method == 'POST':
		try:
			formulario = FormaRegistro(request.POST)
			if formulario.isValid():
				nombre = request.POST['nombre']
				ap_paterno = request.POST['ap_paterno']
				ap_materno = request.POST['ap_materno']
				telefono = request.POST['telefono']
				usuario_nuevo = Usuario(nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, telefono=telefono, area=area)
				usuario_nuevo.save()
			return HttpResponseRedirect('/appella/registrar/')
		except Error as e:
			print 'Error registrando nuevo Usuario: ', e
	else:
		formulario = FormaRegistro()
	return render(request, 'registrar.html', {'form': formulario})


