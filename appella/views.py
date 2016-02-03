from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Usuario, Area
from .forms import FormaRegistro

def registrar(request):
	if request.method == 'POST':
		try:
			formulario = FormaRegistro(request.POST, request.FILES)
			if formulario.is_valid():
				nombre = formulario.cleaned_data['nombre']
				ap_paterno = formulario.cleaned_data['ap_paterno']
				ap_materno = formulario.cleaned_data['ap_materno']
				telefono = formulario.cleaned_data['telefono']
				imagen = formulario.cleaned_data['imagen']
				usuario_nuevo = Usuario(us_nombre=nombre, us_ap_paterno=ap_paterno, us_ap_materno=ap_materno, us_telefono=telefono, us_img=imagen, area=1)
				usuario_nuevo.save()
			return HttpResponseRedirect('/appella/registrar')
		except Exception as e:
			print 'Error registrando nuevo Usuario: ', e
	else:
		formulario = FormaRegistro()
	return render(request, 'registrar.html', {'form': formulario})


