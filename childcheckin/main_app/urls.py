from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/',views.about, name='about'),
path('children/', views.children_index, name='index'),
path('children/<int:child_id>/', views.children_detail, name='detail'),
path('children/create/', views.ChildCreate.as_view(), name='children_create'),
path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='children_update'),
path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='children_delete'),
path('children/<int:child_id>/add_roster/', views.add_roster, name='add_roster'),
path('roster/', views.roster_index, name='roster_index'),
path('accounts/signup/', views.signup, name='signup'),


]