from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login_form, name='login'),
    path('usercform/',views.usercform, name='registration'),
    path('success/',views.slogin),
    path('logout/',views.logout_form, name='logout'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/add/', views.add_company, name='add_company'),
    path('adde/', views.adde, name='adde'),
    path('showe/', views.showe, name='showe'),
   
   
     
  
    
]