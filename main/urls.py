from django.urls import path
from .views import index, login, newsletter

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('newsletter', newsletter, name='newsletter')
]
