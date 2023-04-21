from django.contrib import admin

# Register your models here.
from .models import Child, Roster, Activity

admin.site.register(Child)
admin.site.register(Roster)
admin.site.register(Activity)

