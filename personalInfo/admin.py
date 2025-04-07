from django.contrib import admin

# Register your models here.
from home.models import CommunityPost
from .models import FitnessInformation

admin.site.register(CommunityPost)
admin.site.register(FitnessInformation)
