from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Category, Newsletter
from .forms import NewsletterForm


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
    template = loader.get_template('frontend/views/login.html')
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
        print("dsdf")
        return redirect('index')
    return render(request, '../../ecommercedjango/templates/frontend/views/index.html', {'form': form})
