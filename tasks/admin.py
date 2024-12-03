from django.contrib import admin
from .models import Task
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'status', 'due_date', 'timestamp')

    # Add filters for these fields in the sidebar
    list_filter = ('status', 'due_date', 'timestamp')

    # Add a search bar for these fields
    search_fields = ('title', 'description', 'tags')

    # Specify readonly fields
    readonly_fields = ('timestamp',)

    # Group fields into sections
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'status')
        }),
        ('Additional Information', {
            'fields': ('due_date', 'tags'),
        }),
        ('System Information', {
            'fields': ('timestamp',),
            'classes': ('collapse',),  # Collapse this section in the admin UI
        }),
    )

admin.site.register(Task, TaskAdmin)

# Register your models here.
