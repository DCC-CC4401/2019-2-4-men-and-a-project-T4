from django.urls import path, include
from django.contrib.auth import views, forms

from timePlan import views

# Name space para configurar el espacio de nombres de la aplicación
# Usada con la etiqueta de los templates {% url %]

#name es lo que se busca en url en html
#path  lo que queda arriba en el navegador
urlpatterns = [path('', views.loginView, name='login'),
               path('landing_page/', views.landing_page, name='landing_page'),
               path('auth', views.auth, name='auth'),
               path('profile/', views.userProfile, name='profile'),
               path('upload_img', views.upload_img, name='upload_img'),
               path('register',views.userRegister, name='register_user'),
               path('amigos/', include('amigos.urls')),
               path('logout/', views.logoutView, name='logout'),
               ]
