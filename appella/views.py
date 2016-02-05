from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from models import Usuario, Perdido, Expediente
from django.template import RequestContext
from forms import UploadFileForm, FormaRegistro, FormaPerdido
from django.utils import timezone

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mapa(request):
    template = loader.get_template('mapa.html')
    context = {}
    return HttpResponse(template.render(context, request))

def prueba(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Usuario(area_id=1,us_img = request.FILES['file'])
            newdoc.save(form)
            return HttpResponseRedirect('/appella/')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def handle_uploaded_file(f):
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
#	try:
'''    textoform = request.POST['textform']
    fileform = request.FILES['fileform']
    print 'textform=', textform
    usuario = Usuario(us_nombre=textform, us_img=fileform)
    usuario.save()
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
#	    return render_to_response('index.html', {})
#	except Exception as e:
#	    return render_to_response('index.html', {})
#    return HttpResponse(template.render(context, request))

'
def ejemplo1(request):
	return render_to_response('ejemplo1.html', context_instance=RequestContext(request))
def insertar(request):
	try:
		tit = request.POST['titulo']
		cont = request.POST['contenido']
		print 'titulo=', tit,'\ncontenido=', cont
		a = Articulos(titulo=tit, contenido=cont, fecha = timezone.now())
		a.save()
		return render_to_response('insertar.html', {})
	except Exception as e:
		return render_to_response('insertar.html', {})
'''

def registrar(request):
	if request.method == 'POST':
		try:
			formulario = FormaRegistro(request.POST, request.FILES)
			if formulario.is_valid():
				nombre = formulario.cleaned_data['nombre']
				ap_paterno = formulario.cleaned_data['ap_paterno']
				ap_materno = formulario.cleaned_data['ap_materno']
				telefono = formulario.cleaned_data['telefono']
				imagen = request.FILES['imagen']
				usuario_nuevo = Usuario(us_nombre=nombre, us_ap_paterno=ap_paterno, us_ap_materno=ap_materno, us_telefono=telefono, us_img=imagen)
				usuario_nuevo.save(formulario)
			else:
				print 'Error validando formulario'
				print formulario.errors
			return HttpResponseRedirect('/appella/registrar/')
		except Exception as e:
			print 'Error registrando nuevo Usuario: ', e
	else:
		formulario = FormaRegistro()
	return render(request, 'registrar.html', {'form': formulario})

def perdido(request):
	if request.method == 'POST':
		try:
			formulario = FormaPerdido(request.POST, request.FILES)
			if formulario.is_valid():
				exp = Expediente(ex_estado='Nuevo')
            			exp.save()
				expediente_id = exp.id_expediente
				fecha = timezone.now()
				imagen = request.FILES['imagen']
				texto = formulario.cleaned_data['texto']
				perdido = Perdido(pe_fecha=fecha, pe_img=imagen, pe_texto=texto, expediente_id=expediente_id, usuario_id=1)
				perdido.save(formulario)
			else:
				print 'Error validando formulario'
				print formulario.errors
			return HttpResponseRedirect('/appella/perdido/')
		except Exception as e:
			print 'Error registrando nuevo Perdido: ', e
	else:
		formulario = FormaPerdido()
	return render(request, 'perdido.html', {'form': formulario})
