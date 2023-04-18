from django.shortcuts import render
from .models import Child

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def children_index(request):
  children = Child.objects.all()
  return render(request, 'children/index.html', { 'children': children })

def children_detail(request, child_id):
  child = Child.objects.get(id=child_id)
  return render(request, 'children/detail.html', {'child': child,})

  