import datetime
from email.policy import default
from django.db import models

# Create your models here.

"""
Post
-importance score #entier superieur à 1 et on met donc à zero pour épingler
-date
-title
-theme  
-image
-contenu
-blogPoster 
-joinPiece #url ou #none

"""
class Post(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    date=models.DateField(blank=True,null=True)
    Tag=models.CharField(max_length=500)
    title=models.CharField(max_length=128)
    image=models.ImageField(blank=True,upload_to='imagePost',null=True)
    contenu=models.TextField(blank=True)
    blogPoster=models.CharField(max_length=128,blank=True)
    joinPiece=models.FileField(blank=True,null=True)
    joinLink=models.URLField(blank=True,null=True)

    
    def __str__(self):
        return f"publication de {self.blogPoster} - le : {self.date} titre : {self.title} "
        


    
class Commentaire(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,editable=False)
    email = models.EmailField(blank=True,null=True)
    name = models.CharField(max_length=128)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.TextField()
    date=models.DateField(editable=False,default=datetime.datetime.now(),auto_created=True)
    def __str__(self):
        return f"commentaire  de {self.name} sur {self.post.title} le {self.date.strftime("%d/%m/%Y")}"   
    
class Tag(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=128)
    def __str__(self):
        return f"Tag : {self.name}"  

class Don(models.Model):
    NomDonneur=models.CharField(max_length=250,default="Un Inconnu", blank=True,auto_created=True) 
    email=models.EmailField(max_length=250,null=True,blank=True)
    telephone=models.CharField(max_length=13,default="Inconnu", blank=True,auto_created=True)
    motivation=models.TextField( blank=True,default="Inconnue",auto_created=True) 
    date=models.DateField(editable=False,default=datetime.datetime.now(),auto_created=True)
    montant=models.FloatField()   
    def __str__(self):
        if self.NomDonneur:
           
            return f"Don  de {self.montant} XAF Par {self.NomDonneur} le {self.date.strftime("%d/%m/%Y")}"
        else:
            return f"Don  de {self.montant} XAF Par Un Inconnu le {self.date.strftime("%d/%m/%Y")}"    
 
 
class Volontariat(models.Model):
    Nom_Volontaire=models.CharField(max_length=250) 
    email=models.EmailField(max_length=250)
    telephone=models.CharField(max_length=13)
    motivation=models.TextField(null=True) 
    date=models.DateField(auto_now=True,editable=False)
    ville=models.CharField(max_length=250) 
    activite= models.TextField(null=True, blank=True)    
    
    
class Adhesion(models.Model):
    Proffession=models.CharField(max_length=250,default='Aucune') 
    Nom_Adherateur=models.CharField(max_length=250) 
    email=models.EmailField(max_length=250)
    telephone=models.CharField(max_length=13,null=True,blank=True)
    motivation=models.TextField(null=True) 
    date=models.DateField(editable=False,default=datetime.datetime.now(),auto_created=True)
    ville=models.CharField(max_length=250)  
    def __str__(self):
        return f"Demande d'adhesion de {self.Nom_Adherateur}, numero : {self.telephone} ville : {self.ville} le {self.date}"
    
    

class Souvenir(models.Model):
    descripion=models.CharField(max_length=250) 
    lien=models.URLField(default='#')
    date=models.DateField()
    photo=models.ImageField(upload_to='imageSouvenirs')
    
    
class Partenaire(models.Model):
    nom=models.CharField(max_length=250) 
    lien=models.URLField(default='#')
    photo=models.ImageField(upload_to='imagePartners')
    
class Informations(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True,editable=False)
    tel=models.CharField(max_length=30)
    fax=models.CharField(max_length=30)
    email=models.CharField(max_length=500)
    lieu=models.CharField(max_length=500)
    facebook=models.CharField(max_length=500)
    twitter=models.CharField(max_length=500)
    autre=models.CharField(max_length=500)
    web=models.CharField(max_length=500)
    qui_sommes_nous=models.TextField()
    
class Mot_president(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True,editable=False)
    titre=models.CharField(max_length=500)
    sous_titre=models.CharField(max_length=500)
    contenu=models.TextField()
    signature=models.CharField(max_length=500)
    photo=models.ImageField(upload_to='imagePresi')