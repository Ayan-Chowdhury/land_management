from django.db import models


class Company(models.Model):
    CompanyCode = models.CharField(max_length=5)
    CompanyName = models.CharField(max_length=8)

    def __str__(self):
        return self.CompanyName


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

class Project(models.Model):
    Project_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=100, blank=False, editable=True)

    def __str__(self):
        return self.Project_name


class Detail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_number = models.CharField(max_length=50, editable=False)
    deed_number = models.PositiveIntegerField(max_length=50, editable=False)
    registration_date = models.DateField( blank=True, null=True)
    mutation_status_number = models.CharField(max_length=100, blank=True, null=True)
    mutation_status_date = models.DateField(blank=True, null=True)
    mutation_status_dcr = models.FileField(upload_to='mutation_status_dcr/', blank=True, null=True)
    last_seller = models.CharField(max_length=255, blank=True)
    # buyer = models.CharField(max_length=255, blank=True, null=True)
    buyer = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name_of_buyer = models.CharField(max_length=255, blank=True, null=True)
    type_of_deed = models.ForeignKey(Deed_Type, on_delete=models.SET_NULL, null=True, blank=True )
    # type_of_deed = models.CharField(max_length=100, blank=True, null=True)
    land_area_in_decimal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deed_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    purchase_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    mouja = models.CharField(max_length=255, blank=False, null=False)
    khatian_cs = models.CharField(max_length=100, blank=True, null=True)
    khatian_sa = models.CharField(max_length=100, blank=True, null=True)
    khatian_rs = models.CharField(max_length=100, blank=True, null=True)
    khatian_bs_brs = models.CharField(max_length=100, blank=True, null=True)
    khatian_city_jorip = models.CharField(max_length=100, blank=True, null=True)

    dag_cs = models.CharField(max_length=100, blank=True, null=True)
    dag_sa = models.CharField(max_length=100, blank=True, null=True)
    dag_rs = models.CharField(max_length=100, blank=True, null=True)
    dag_bs_brs = models.CharField(max_length=100, blank=True, null=True)
    dag_city_jorip = models.CharField(max_length=100, blank=True, null=True)
    type_of_land = models.ForeignKey(Land_Type, on_delete=models.SET_NULL, blank=True, null=True)
    # type_of_land = models.CharField(max_length=100, blank=True, null=True)
    khajana_status=models.ForeignKey(khajana_payment, on_delete=models.SET_NULL, blank=True, null=True)
    # khajana_status = models.CharField(max_length=50, blank=True, null=True)
    khajana_year=models.ForeignKey(Fiscal_Year, on_delete=models.SET_NULL, blank=True, null=True)
    # mortgage_bank_name = models.CharField(max_length=100, null=True, blank=True)
    mortgage_bank_name = models.ForeignKey(Bank_List, on_delete=models.SET_NULL, blank=True, null=True)
    mortgage_deed = models.FileField(upload_to='mortgage_deeds/', blank=True, null=True)
    mortgage_poa_deeds = models.FileField(upload_to='poa_deeds/', blank=True, null=True)
    mortgage_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.file_number:
            # Get the latest file number for the current project
            last_file_number = Detail.objects.filter(project=self.project).order_by('file_number').last()
            if last_file_number and last_file_number.file_number:
                # Extract the numeric part of the last file number
                last_number = int(last_file_number.file_number.split('-')[1])  # Split by '-' and convert to int
                new_number = last_number + 1
            else:
                new_number = 1  # Start from D-001 if no existing file number

            # Format the new file number
            self.file_number = f'D-{new_number:03}'

        # Auto-increment the deed number for each details entry
        last_deed_number = Detail.objects.filter(project=self.project).order_by('deed_number').last()
        if last_deed_number:
            self.deed_number = last_deed_number.deed_number + 1
        else:
            self.deed_number = 1  # Start from 1 if no existing deed number

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Deed {self.deed_number} for {self.project}"
