from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Child, Roster

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

class RosterCreate(LoginRequiredMixin, CreateView):
  model = Roster
  fields = ['date', 'age_group', 'checkin_status', 'caregiver', 'dropped_off_by', 'enrolled_status']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
   
   

  