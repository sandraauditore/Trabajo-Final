from django import forms



#class GaleriaFormulario(forms.Form):

   # Nombre = forms.CharField()
   # Descripcion = forms.CharField()
   # Imagen = forms.ImageField() 
   # Precio = forms.FloatField()


class ContactoFormulario(forms.Form):
    
    Nombre = forms.CharField()
    Email = forms.EmailField()
    Mensaje = forms.CharField()
