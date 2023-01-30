from django.contrib import admin
from . models import Article,Categorie,Commentaire,Contact

# Register your models here.

admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Commentaire)
admin.site.register(Contact)

