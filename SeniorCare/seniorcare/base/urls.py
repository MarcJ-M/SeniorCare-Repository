from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_page/', views.register_page, name='register_page'),
    path('main_page/', views.main_page, name='main_page'), 
    path('home_page/', views.home_page, name='home_page'),   
    path('update_page/', views.update_page, name='update_page'),
    path('update_viewinfo_page/<int:id>', views.update_viewinfo_page, name='update_viewinfo_page'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name = 'delete'),

     path('search/', views.search, name='search'),
     path('search1/', views.search1, name='search1'),

    path('claim_page/', views.claim_page, name='claim_page'),  
    path('claim_detail_page/<int:id>', views.claim_detail_page, name='claim_detail_page'),
    path('claimed_succesfully/<int:id>', views.claimed_succesfully, name='claimed_succesfully'),
    path('claimed_success/<int:id>', views.claimed_success, name='claimed_success'),
    path('claim_verify_page/', views.claim_verify_page, name='claim_verify_page'),
    path('claim_summary_page/', views.claim_summary_page, name='claim_summary_page'),
    path('download_summary/', views.download_summary, name='download_summary'),
]
