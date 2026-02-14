from django.contrib import admin
from django.utils.html import format_html
from .models import Experiment

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'slug', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview', 'created_at')
    
    fieldsets = (
        ('معلومات التجربة', {
            'fields': ('title', 'description', 'slug')
        }),
        ('الوسائط', {
            'fields': ('image', 'image_preview')
        }),
        ('الإعدادات', {
            'fields': ('is_active', 'created_at')
        }),
    )
    
    def image_preview(self, obj):
        """Display image preview in admin."""
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 8px;" />', obj.image.url)
        return "لا توجد صورة"
    image_preview.short_description = 'معاينة الصورة'
