from django.contrib import admin
from datetime import date
from django import forms
from rangefilter.filters import DateRangeFilter
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.templatetags.static import static
from .models import Project, Detail, Fiscal_Year, Status, Land_Type
from .forms import ProjectForm
from radiant_land.widgets import PastCustomDatePickerWidget


class DetailInlineForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()

        # Find the current fiscal year based on today's date
        current_fiscal_year = Fiscal_Year.objects.filter(start_date__lte=today, end_date__gte=today).first()

        # Set the default khajana_year if available
        if current_fiscal_year:
            self.fields['khajana_year'].initial = current_fiscal_year


class DetailInline(admin.StackedInline):
    model = Detail
    extra = 0 # No extra blank fields
    # fields = ['registration_date', 'buyer', 'land_area_in_decimal']


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ['Project_name', 'Division', 'District', 'Upazilla']
    # list_display = ['Project_name','Address']
    inlines = [DetailInline]  # Inline address info on project page
    list_filter = ['Project_name']  # Filter by project name

    class Media:
        js = [
            static('assets/admin/js/jquery.init.js'),
            static('assets/admin/js/cascading_dropdown.js'),  # Path to your custom JS file
        ]


class DetailAdmin(admin.ModelAdmin):
    list_display = ['project', 'file_number', 'deed_number', 'registration_date', 'khajana_year', 'dag_cs','dag_sa','dag_rs','dag_bs_brs','dag_city_jorip',  'buyer', 'mouja','land_area_in_decimal','type_of_land']
    list_filter = ['project',('registration_date', DateRangeFilter), 'buyer']  # Filters for Address details
    search_fields = ['deed_number', 'dag_cs','dag_sa','dag_rs','dag_bs_brs','dag_city_jorip','file_number', 'buyer__CompanyName', 'type_of_deed__Deed_Name']  # Search bar fields


admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail, DetailAdmin)

