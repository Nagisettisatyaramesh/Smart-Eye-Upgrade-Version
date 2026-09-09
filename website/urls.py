from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('why-smarteye/', views.why_smarteye, name='why_smarteye'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('workspace/', views.workspace, name='workspace'),
]
