from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Child, Roster, Activity
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
  id_list = child.activities.all().values_list('id')
  activities_child_doesnt_have = Activity.objects.exclude(id__in=id_list)
  return render(request, 'children/detail.html', {'child': child,'roster_form':roster_form,'activities': activities_child_doesnt_have})

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

def add_roster(request, child_id):
  # create a ModelForm instance using the data in request.POST
   form = RosterForm(request.POST)
  # validate the form
   if form.is_valid():
    # don't save the form to the db until it
    # has the child_id assigned
    new_roster = form.save(commit=False)
    new_roster.user = request.user
    new_roster.child_id = child_id
    new_roster.save()
   return redirect('detail', child_id=child_id)

class RosterCreate(LoginRequiredMixin, CreateView):
  model = Roster
  fields = ['date', 'age_group', 'time_entered', 'caregiver', 'dropped_off_by', 'enrolled_status']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class ActivityList(LoginRequiredMixin, ListView):
  model = Activity

class ActivityDetail(LoginRequiredMixin, DetailView):
  model = Activity

class ActivityCreate(LoginRequiredMixin, CreateView):
  model = Activity
  fields = '__all__'

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['name', 'description', 'duration']

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities'

  
@login_required
def assoc_activity(request, child_id, activity_id):
  Child.objects.get(id=child_id).activities.add(activity_id)
  return redirect('detail', child_id=child_id)

@login_required
def unassoc_Activity(request, child_id, activity_id):
  Child.objects.get(id=child_id).activities.remove(activity_id)
  return redirect('detail', child_id=child_id)

  
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

  


   
   

  