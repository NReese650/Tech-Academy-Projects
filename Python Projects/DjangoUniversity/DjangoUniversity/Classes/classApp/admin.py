from django.contrib import admin
from .models import UniversityClasses
from .models import UniversityCampus

# Register your models here.
admin.site.register(UniversityClasses)
admin.site.register(UniversityCampus)