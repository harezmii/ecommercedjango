from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Product, Category, Newsletter
from .forms import NewsletterForm, RegisterForm, LoginForm


# Create your views here.

def index(request):
    template = loader.get_template('frontend/views/index.html')
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('frontend/views/user/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('frontend/views/user/register.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            Newsletter.objects.create(name=name, email=email)

            return redirect('index')
    else:
        return redirect('index')
    return render(request, 'frontend/views/index.html')


def loginPost(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            from django.contrib.auth import authenticate, login
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/login")
    return render(request, 'frontend/views/user/login.html')


def registerPost(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            from django.contrib.auth.models import User
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            user = User.objects.create_user(username=username, email=email, password=password)
            return render(request, 'frontend/views/index.html')

    return render(request, 'frontend/views/user/register.html')


def passwordReset(request):
    template = loader.get_template('frontend/views/user/passwordReset.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def passwordResetPost(request):
    if request.method == "POST":
        password = request.POST["password"]
        passwordAgain = request.POST["passwordAgain"]

        if password == passwordAgain:
            from django.contrib.auth.models import User
            user = User.objects.get(username=request.user)
            user.set_password(password)
        else:
            messages.error(request, "Şifreler uyuşmuyor")
            return redirect("/passwordReset")
