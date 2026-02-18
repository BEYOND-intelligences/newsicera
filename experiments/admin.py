from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Experiment, Subject, Tag, Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    fields = ('title', 'description', 'image', 'order', 'is_active')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 4px;" />', obj.icon.url)
        return "لا توجد أيقونة"
    icon_preview.short_description = 'معاينة الأيقونة'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'image_preview', 'get_tags', 'current_status', 'created_at', 'delete_button')
    search_fields = ('title', 'description', 'physical_law')
    list_filter = ('subject', 'is_active', 'created_at', 'tags')
    list_editable = ('subject',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview', 'created_at')
    filter_horizontal = ('tags',)
    
    fieldsets = (
        ('معلومات التجربة', {
            'fields': ('title', 'subject', 'description', 'slug', 'tags')
        }),
        ('التفاصيل العلمية', {
            'fields': ('physical_law', 'tools_needed', 'steps', 'video_url')
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

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'التصنيفات'

    def current_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">نشط</span>')
        return format_html('<span style="color: red;">غير نشط</span>')
    current_status.short_description = 'الحالة'

    def delete_button(self, obj):
        # Create a delete button that links to the delete page for this object
        delete_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_delete', args=[obj.pk])
        return format_html('<a class="button" href="{}" style="background-color: #bf2d2d; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none;">حذف</a>', delete_url)
    delete_button.short_description = 'إجراءات'
