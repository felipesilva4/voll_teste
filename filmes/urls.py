from django.urls import path
from .views import Filmes_Create, Filmes_List
from .views import Filmes_Detail, Filmes_Update, Filmes_Delete
from .views import signup

#Registro de url
urlpatterns = [
    path('create/', Filmes_Create.as_view(), name='filmes_create'),
    path ('list/',Filmes_List.as_view(), name='filmes_list'),
    path ('detail/<int:pk>', Filmes_Detail.as_view(), name='filmes_detail'),
    path ('update/<int:pk>', Filmes_Update.as_view(), name= 'filmes_update'),
    path ('delete/<int:pk>', Filmes_Delete.as_view(), name='filmes_delete'),
    path ('cadastro/',signup, name = 'cadastro' )
]