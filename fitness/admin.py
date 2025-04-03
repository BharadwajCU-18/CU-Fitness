from django.contrib import admin
from fitness.models import FitnessReport

class FitnessReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'steps', 'cardio_time', 'cool_down_time')
    fields = ('user', 'date', 'steps', 'cardio_time', 'cool_down_time')
    search_fields = ('user__username',)

admin.site.register(FitnessReport, FitnessReportAdmin)


# admin.site.register(FitnessReport)  