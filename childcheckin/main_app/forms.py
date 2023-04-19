from django.forms import ModelForm
from .models import Roster

class RosterForm(ModelForm):
  class Meta:
    model = Roster
    fields = ['date', 'age_group', 'checkin_status', 'caregiver', 'dropped_off_by', 'enrolled_status']
