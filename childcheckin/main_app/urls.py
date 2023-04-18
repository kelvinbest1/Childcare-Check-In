from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/',views.about, name='about'),
   path('children/', views.children_index, name='index'),
   path('children/<int:child_id>/', views.children_detail, name='detail'),
   path('accounts/signup/', views.signup, name='signup'),

]