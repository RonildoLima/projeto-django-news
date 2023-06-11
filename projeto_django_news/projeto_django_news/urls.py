from app_django_news import views
from django.urls import path

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('contato/',views.contato,name='contato'),
    path('noticia/',views.noticia,name='noticia'),
    path('termo/',views.termo,name='termo'),
    path('cancelar/',views.cancelar,name='cancelar'),

]
