from django.contrib import admin
from datetime import date
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.templatetags.static import static
from .models import Project, Detail, Fiscal_Year
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
            # static('admin/js/jquery.init.js'),
            static('admin/js/cascading_dropdown.js'),  # Path to your custom JS file
        ]

    # def get_extra_js(self):
    #     return mark_safe(f"""
    #        <script>
    #            (function($) {{
    #                $(document).ready(function() {{
    #                    $('#id_Division').change(function() {{
    #                        var divisionId = $(this).val();
    #                        $.ajax({{
    #                            url: '{reverse('filter_districts')}?division=' + divisionId,
    #                            success: function(data) {{
    #                                $('#id_District').empty();
    #                                $.each(data.options, function(index, option) {{
    #                                    $('#id_District').append('<option value="' + option.id + '">' + option.name + '</option>');
    #                                }});
    #                                $('#id_Upazilla').empty();  // Clear Upazilla dropdown
    #                            }}
    #                        }});
    #                    }});
    #
    #                    $('#id_District').change(function() {{
    #                        var districtId = $(this).val();
    #                        $.ajax({{
    #                            url: '{reverse('filter_upazillas')}?district=' + districtId,
    #                            success: function(data) {{
    #                                $('#id_Upazilla').empty();
    #                                $.each(data.options, function(index, option) {{
    #                                    $('#id_Upazilla').append('<option value="' + option.id + '">' + option.name + '</option>');
    #                                }});
    #                            }}
    #                        }});
    #                    }});
    #                }});
    #            }})(django.jQuery);
    #        </script>
    #        """)
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['extra_js'] = self.get_extra_js()
    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)
    #
    # def add_view(self, request, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['extra_js'] = self.get_extra_js()
    #     return super().add_view(request, form_url, extra_context=extra_context)


class DetailAdmin(admin.ModelAdmin):
    list_display = ['project', 'deed_number', 'registration_date', 'buyer', 'mouja','land_area_in_decimal']
    # list_filter = ['project', 'registration_date', 'type_of_land']  # Filters for Address details
    search_fields = ['deed_number', 'file_number', 'buyer__CompanyName', 'type_of_deed__Deed_Name']  # Search bar fields


admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail, DetailAdmin)

