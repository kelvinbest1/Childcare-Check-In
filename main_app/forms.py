from django.forms import ModelForm
from .models import Roster


 
class RosterForm(ModelForm):
  class Meta:
   model = Roster
   fields = ['date','time_entered', 'age_group',  'caregiver', 'dropped_off_by','enrolled_status']
  
