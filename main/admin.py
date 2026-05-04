from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'order', 'client_or_company', 'created_at')
    list_editable = ('featured', 'order')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'description', 'tools_used', 'client_or_company')
    fieldsets = (
        ('Core Info', {
            'fields': ('title', 'category', 'short_description', 'description', 'image', 'video', 'project_file')
        }),
        ('Details', {
            'fields': ('tools_used', 'outcome', 'client_or_company', 'duration')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')


admin.site.site_header = 'Rosemary Dimakunne — Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Manage Your Portfolio'
