from django import forms 

class form_escuela(forms.Form):
    
    disciplina = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
   

class inscripcion_alumnos(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=50)
    email = forms.EmailField()


class form_entrenador(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=50)
    email = forms.EmailField()

