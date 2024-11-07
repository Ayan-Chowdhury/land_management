# forms.py
from django import forms
from .models import Project, Division, District, Upazilla

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Project_name', 'Division', 'District', 'Upazilla']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()
        self.fields['Upazilla'].queryset = Upazilla.objects.none()

        if 'Division' in self.data:
            try:
                division_code = self.data.get('Division')
                self.fields['District'].queryset = District.objects.filter(DivisionCode=division_code)
            except (ValueError, TypeError):
                pass  # invalid input from client; ignore and default to empty queryset

        if 'District' in self.data:
            try:
                district_code = self.data.get('District')
                self.fields['Upazilla'].queryset = Upazilla.objects.filter(DistrictCode=district_code)
            except (ValueError, TypeError):
                pass  # invalid input from client; ignore and default to empty queryset
