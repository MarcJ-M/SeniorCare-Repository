from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_page/', views.register_page, name='register_page'),
    path('main_page/', views.main_page, name='main_page'), 
    path('home_page/', views.home_page, name='home_page'),   
    path('update_page/', views.update_page, name='update_page'),
    path('update_viewinfo_page/', views.update_viewinfo_page, name='update_viewinfo_page'),
    path('claim_page/', views.claim_page, name='claim_page'),  
    path('claim_detail_page/<int:id>', views.claim_detail_page, name='claim_detail_page') 
]
