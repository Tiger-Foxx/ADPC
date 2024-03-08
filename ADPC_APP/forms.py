from django import forms
from ADPC_APP.models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['post','name','email', 'message']
        
        
class DonForm(forms.ModelForm):
    class Meta:
        model = Don
        fields = ['NomDonneur','telephone','email', 'motivation','montant']

class AdhesionForm(forms.ModelForm):
    class Meta:
        model = Adhesion
        fields = ['Nom_Adherateur','telephone','email', 'motivation','ville']

class VolontariatForm(forms.ModelForm):
    class Meta:
        model = Volontariat
        fields = ['Nom_Volontaire','telephone','email', 'motivation','ville','activite']  

