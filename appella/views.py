from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from models import Usuario
from django.template import RequestContext
from forms import UploadFileForm
from models import Area
from .forms import FormaRegistro
# Create your views here.
def index(request):
#	return render_to_response('index.html', context_instance=RequestContext(request))
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def prueba(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            area = Area(ar_lat1='212121')
            area.save()
            newdoc = Usuario(area_id=1,us_img = request.FILES['file'])
            newdoc.save(form)
#            fileform = request.FILES['file'].read()
#            print "\nfileform=",fileform
#            shutil.copy(fileform, "media/"+str(fileform))
#            handle_uploaded_file(fileform)
            return HttpResponseRedirect('/ella/')
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
				imagen = formulario.cleaned_data['imagen']
				usuario_nuevo = Usuario(us_nombre=nombre, us_ap_paterno=ap_paterno, us_ap_materno=ap_materno, us_telefono=telefono, us_img=imagen, area=1)
				usuario_nuevo.save()
			return HttpResponseRedirect('/appella/registrar')
		except Exception as e:
			print 'Error registrando nuevo Usuario: ', e
	else:
		formulario = FormaRegistro()
	return render(request, 'registrar.html', {'form': formulario})

