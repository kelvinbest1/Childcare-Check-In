from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Child, Roster
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RosterForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def children_index(request):
  children = Child.objects.all()
  return render(request, 'children/index.html', { 'children': children })

@login_required
def children_detail(request, child_id):
  child = Child.objects.get(id=child_id)
  roster_form = RosterForm()
  return render(request, 'children/detail.html', {'child': child,})

class ChildCreate(LoginRequiredMixin, CreateView):
  model = Child
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ChildUpdate(LoginRequiredMixin,UpdateView):
  model = Child
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['age', 'note']

class ChildDelete(DeleteView):
  model = Child
  success_url = '/children'

  

class RosterCreate(LoginRequiredMixin, CreateView):
  model = Roster
  fields = ['date', 'age_group', 'checkin_status', 'caregiver', 'dropped_off_by', 'enrolled_status']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
     form = UserCreationForm(request.POST)
     if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
  else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

   
   

  