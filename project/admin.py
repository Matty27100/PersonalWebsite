from django.contrib import admin
from project.models import Project, Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_range', 'order')
    list_editable = ('order',)  # Allow editing the order directly from the list view
    ordering = ('order',)  # Default ordering in admin

admin.site.register(Project)