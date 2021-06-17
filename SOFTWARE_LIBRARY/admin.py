from django.contrib import admin

from SOFTWARE_LIBRARY.models import Software, Category, License, Developer

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_filter = ['software_category', 'software_developer']
    search_fields = ['software_name', 'software_category', 'software_developer', 'software_jlicense']
    list_display = ['software_name', 'software_version', 'software_license', 'software_category', 'software_developer',
                    'software_source', 'software_logo', 'software_image']
    list_per_page = 20
    ordering = ['software_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ['category_name']
    ordering = ['category_name']


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    search_fields = ['license_name']
    list_display = ['license_name']
    ordering = ['license_name']


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    search_fields = ['developer_name']
    list_display = ['developer_name', 'developer_web_site']
    ordering = ['developer_name']
