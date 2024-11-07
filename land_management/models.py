import os
from django.db import models
from django.core.exceptions import ValidationError

def get_map_pic_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")  # Use underscores to avoid spaces
    return os.path.join('documents', project_name, 'map_pictures', filename)
def get_deed_file_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")  # Use underscores to avoid spaces
    return os.path.join('documents', project_name, 'deed_file', filename)

def get_mutation_dcr_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")  # Use underscores to avoid spaces
    return os.path.join('documents', project_name, 'mutation_dcr', filename)


def get_khajana_document_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")
    return os.path.join('documents', project_name, 'khajana_document', filename)


def get_khatian_document_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")
    return os.path.join('documents', project_name, 'khatian_document', filename)


def get_mortgage_deed_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")
    return os.path.join('documents', project_name, 'Mortgage/mortgage_deed', filename)


def get_mortgage_poa_deed_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")
    return os.path.join('documents', project_name, 'Mortgage/poa_deed', filename)


def get_extra_document_upload_path(instance, filename):
    project_name = instance.project.Project_name.replace(" ", "_")
    return os.path.join('documents', project_name, 'extra_document', filename)


def validate_file_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.pdf']  # Add your valid extensions here
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}')


class Company(models.Model):
    CompanyCode = models.CharField(max_length=5)
    CompanyName = models.CharField(max_length=8)

    def __str__(self):
        return self.CompanyName


class Status(models.Model):
    status_N=models.CharField(max_length=6)

    def __str__(self):
        return self.status_N


class Deed_Type(models.Model):
    Deed_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Deed_Name


class Land_Type(models.Model):
    land_type = models.CharField(max_length=20)

    def __str__(self):
        return self.land_type


class Bank_List(models.Model):
    bank_name=models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name


class khajana_payment(models.Model):
    khajana_status=models.CharField(max_length=10)

    def __str__(self):
        return self.khajana_status


class Fiscal_Year(models.Model):
    fiscal_year=models.CharField(max_length=10)
    start_date= models.DateField()
    end_date= models.DateField()

    def __str__(self):
        return self.fiscal_year

    # def is_near_end(self):
    #     today=datetime.now().date()
    #     two_months_from_now=today+timedelta(days=60)
    #     return today<=self.end_date <= two_months_from_now


class Division(models.Model):
    DivisionCode = models.CharField(max_length=2, unique=True, primary_key=True)  # Set as primary key
    DivisionName = models.CharField(max_length=50)

    def __str__(self):
        return self.DivisionName


class District(models.Model):
    DivisionCode = models.ForeignKey(
        Division,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        to_field="DivisionCode"
    )
    DistrictCode = models.CharField(max_length=2, unique=True, primary_key=True)  # Set as primary key
    DistrictName = models.CharField(max_length=50)

    def __str__(self):
        return self.DistrictName


class Upazilla(models.Model):
    DistrictCode = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        to_field="DistrictCode"
    )
    UpazillaCode = models.CharField(max_length=4, unique=True, primary_key=True)  # Set as primary key
    UpazillaName = models.CharField(max_length=50)

    def __str__(self):
        return self.UpazillaName


class Project(models.Model):
    Project_name = models.CharField(max_length=100)
    Division = models.ForeignKey(Division, on_delete=models.CASCADE)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    Upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_name


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_number = models.CharField(max_length=50, editable=False)
    deed_number = models.PositiveIntegerField( blank=False,null=False)
    deed_file = models.FileField(upload_to=get_deed_file_upload_path, blank=True, null=True, validators=[validate_file_extension])
    registration_date = models.DateField( blank=True, null=True)
    type_of_deed = models.ForeignKey(Deed_Type, on_delete=models.SET_NULL, null=True, blank=True)
    last_seller = models.CharField(max_length=100, blank=True)
    # buyer = models.CharField(max_length=100, blank=True, null=True)
    buyer = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name_of_buyer = models.CharField(max_length=100, blank=True, null=True)

    land_area_in_decimal = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    deed_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    actual_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mouja = models.CharField(max_length=100, blank=False, null=False)
    jl_no=models.CharField(max_length=100, blank=True, null=True)
    map_pic=models.FileField(upload_to=get_map_pic_upload_path, blank=True,null=True,validators=[validate_file_extension])
    #Khatian_Records:
    khatian_cs = models.CharField(max_length=100, blank=True, null=True)
    khatian_sa = models.CharField(max_length=100, blank=True, null=True)
    khatian_rs = models.CharField(max_length=100, blank=True, null=True)
    khatian_bs_brs = models.CharField(max_length=100, blank=True, null=True)
    khatian_city_jorip = models.CharField(max_length=100, blank=True, null=True)
    khatian_document= models.FileField(upload_to=get_khatian_document_upload_path, blank=True, null=True, validators=[validate_file_extension])
    #Dag_Records:
    dag_cs = models.CharField(max_length=100, blank=True, null=True)
    dag_sa = models.CharField(max_length=100, blank=True, null=True)
    dag_rs = models.CharField(max_length=100, blank=True, null=True)
    dag_bs_brs = models.CharField(max_length=100, blank=True, null=True)
    dag_city_jorip = models.CharField(max_length=100, blank=True, null=True)
    # dag_document=models.FileField(upload_to=get_dag_document_upload_path, blank=True, null=True, validators=[validate_file_extension])

    type_of_land = models.ForeignKey(Land_Type, on_delete=models.SET_NULL, blank=True, null=True)

    #Mutation_Records
    mutation_status_date = models.DateField(blank=True, null=True)
    mutation_status_number = models.CharField(max_length=100, blank=True, null=True)
    mutation_dcr_status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
    mutation_status_dcr = models.FileField(upload_to=get_mutation_dcr_upload_path, blank=True, null=True, validators=[validate_file_extension])

    holding_tax=models.ForeignKey(Fiscal_Year, on_delete=models.SET_NULL, blank=True, null=True, related_name='holding_tax_details')
    service_charge=models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    #Khajana_Info
    khajana_status=models.ForeignKey(khajana_payment, on_delete=models.SET_NULL, blank=True, null=True)
    khajana_year=models.ForeignKey(Fiscal_Year, on_delete=models.SET_NULL, blank=True, null=True, related_name='khajana_year_details')
    khajana_document=models.FileField(upload_to=get_khajana_document_upload_path, blank=True, null=True, validators=[validate_file_extension])

    #Mortgage_Information
    mortgage_bank_name = models.ForeignKey(Bank_List, on_delete=models.SET_NULL, blank=True, null=True)
    mortgage_deed_number = models.CharField(max_length=10, blank=True, null=True)
    mortgage_deed = models.FileField(upload_to=get_mortgage_deed_upload_path, blank=True, null=True, validators=[validate_file_extension])
    mortgage_poa_deed_number = models.CharField(max_length=10, blank=True, null=True)
    mortgage_poa_deeds = models.FileField(upload_to=get_mortgage_poa_deed_upload_path, blank=True, null=True, validators=[validate_file_extension])
    mortgage_date = models.DateField(blank=True, null=True)
    extra_document = models.FileField(upload_to=get_extra_document_upload_path, blank=True, null=True, validators=[validate_file_extension])
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.file_number:
            # Fetch the district name from the related project
            district_name = self.project.District.DistrictName  # Use DistrictName as the field name for District
            district_prefix = district_name.replace(" ", "")  # Remove spaces if needed

            # Get the latest file number for the current district
            last_file_number = Detail.objects.filter(project__District=self.project.District).order_by(
                'file_number').last()

            if last_file_number and last_file_number.file_number:
                # Extract the numeric part of the last file number
                last_number = int(last_file_number.file_number.split('-')[-1])  # Split by '-' and convert to int
                new_number = last_number + 1
            else:
                new_number = 1  # Start from District-001 if no existing file number

            # Format the new file number
            self.file_number = f'{district_prefix}-{new_number:03}'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Deed {self.deed_number} for {self.project}"
