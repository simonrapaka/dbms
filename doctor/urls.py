from django.urls import path
from . import views

urlpatterns = [
        path('', views.doc, name='ghms-doc'),
        path('pat/', views.pat, name='ghms-doc-pat')
]