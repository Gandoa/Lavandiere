from django import forms
from .models import CommandeModel, ContactModel
   
# create a ModelForm
class CommandeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = CommandeModel
        fields = "__all__"




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
