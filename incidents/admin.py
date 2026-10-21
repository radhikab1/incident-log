from django.contrib import admin
from .models import Service, Incident

# Register your models here.
admin.site.register(Service)
admin.site.register(Incident)