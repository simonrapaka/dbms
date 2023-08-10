from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ghms-home'),
    path('login/pat',views.loginp, name='ghms-login-pat'),
    path('login/doc',views.logind, name='ghms-login-doc'),
    path('reg/',views.register, name='ghms-register'),
]
