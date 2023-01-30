from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
import datetime

User = get_user_model()

class MyAuthor (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="authors")
  
    # standards

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user.username


class Categorie (models.Model):
    nom =models.CharField(max_length=150)

    #Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    prix = models.CharField(max_length=250)
    ancien_prix = models.CharField(max_length=250)
    image = models.ImageField(upload_to='articles') # permet d'indiquer le fichier où recuperer les images

    # Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.titre


class Commentaire(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    objet = models.CharField(max_length=150)
    email = models.EmailField()
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    # Standards
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        self.nom= models.SlugField("commenter par" + str(self.name)+ "a"+ str(self.date_add))
        super.save (*args,**kwargs)
    def __str__(self) :
        return self.commentaire



class Avis(models.Model):
    like = models.BooleanField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='avis')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    # Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.like

from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email        