from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('patientreg',views.patientreg,name='patientreg'),
    path('doctorreg',views.doctorreg,name='doctorreg'),
    path('ahome',views.ahome,name='ahome'),
    path('dhome',views.dhome,name='dhome'),
    path('phome',views.phome,name='phome'),
    path('dreg',views.dreg,name='dreg'),
    path('preg',views.preg,name='preg'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('dodet',views.dodet,name='dodet'),
    path('pdet',views.pdet,name='pdet'),
]