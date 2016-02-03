from django import forms

MIN_CELULAR = 60000000
MAX_CELULAR = 79999999

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class FormaRegistro(forms.Form):
	nombre = forms.CharField(label='Nombre: ', max_length=25)
	ap_paterno = forms.CharField(label='Apellido Paterno: ', max_length=25)
	ap_materno = forms.CharField(label='Apellido Materno: ', max_length=25)
	telefono = forms.IntegerField(min_value=MIN_CELULAR, max_value=MAX_CELULAR)
	imagen = forms.FileField(max_length=256)
