# forms.py
from django import forms
from .models import Project, Division, District, Upazilla

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Project_name', 'Division', 'District', 'Upazilla']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'Division' in self.data:
            division_id = self.data.get('Division')
            self.fields['District'].queryset = District.objects.filter(DivisionCode=division_id)
        elif self.instance.pk:
            self.fields['District'].queryset = District.objects.filter(DivisionCode=self.instance.Division)

        if 'District' in self.data:
            district_id = self.data.get('District')
            self.fields['Upazilla'].queryset = Upazilla.objects.filter(DistrictCode=district_id)
        elif self.instance.pk:
            self.fields['Upazilla'].queryset = Upazilla.objects.filter(DistrictCode=self.instance.District)
