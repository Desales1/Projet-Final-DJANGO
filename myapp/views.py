from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from myapp.models import*
from django.shortcuts import render
from .forms import ContactForm
  
def index(request):
	articles = Article.objects.all()

	datas = {
		articles:"articles"
	}
	return render(request, 'index4.html', datas)

def about_us(request):
    datas = {}
    return render(request, 'about_us.html', datas)




def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact-us.html', context)



def product_details(request):
	context = {}
	return render(request, 'product_details.html', context)

def category(request):
	category = Categorie.object.filter(statut = True)
	context = {
		'category': Categorie
	}
	return render(request, 'category.html', context)

def blog_list(request):
	context = {}
	return render(request, 'blog_list.html', context)

def blog_details(request):
	context = {}
	return render(request, 'blog_details.html', context)

def cart_page(request):
	context = {}
	return render(request, 'cart_page.html', context)

def checkout_page(request):
	context = {}
	return render(request, 'checkout_page.html', context)

def order_confirmation(request):
	context = {}
	return render(request, 'order-confirmation.html', context)

def product_grid(request):
	context = {}
	return render(request, 'product_grid.html', context)

def my_account(request):
	context = {}
	return render(request, 'my-account.html', context)


def RegisterView(request):
	form = UserCreationForm()
	if request.method =='POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()  
			messages.success(request="Vous avez été bien connecté.  ")
			return redirect ('register')
		else:
			messages.error(request, form.errors )
	return render(request, 'register.html')


def login (request):
	if request.method == "POST":
		Username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,Username=Username,password=password)
		if user is not None and user.is_active:
			login(request,user)
			messages.success(request, 'Bienvenue')
			return redirect ('login ')
		else:
				messages.error(request,"erreur d'auyhentification",)
	return render(request, 'login.html', )


@login_required
def deconnexion (request):
	logout(request)
	return redirect ('index4.html')



