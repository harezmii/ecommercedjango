from django.urls import path
from .views import index, login, newsletter, register, loginPost, registerPost, passwordReset, passwordResetPost

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('loginPost', loginPost, name='loginPost'),
    path('register', register, name='register'),
    path('registerPost', registerPost, name='registerPost'),
    path('newsletter', newsletter, name='newsletter'),
    path('passwordReset', passwordReset, name='passwordReset'),
    path('passwordResetPost', passwordResetPost, name='passwordResetPost')
]
