from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'company_size', 'created_at')
    list_filter = ('company_size', 'created_at')
    search_fields = ('name', 'email', 'company')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
