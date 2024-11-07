from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Project, Detail, Fiscal_Year, District,Upazilla
from django.http import JsonResponse, FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt
from datetime import datetime, timedelta
import pprint
  # This will show all attributes in the detail object

def filter_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(DivisionCode_id=division_id).values('DistrictCode', 'DistrictName')
    return JsonResponse(list(districts), safe=False)

def filter_upazillas(request):
    district_id = request.GET.get('district')
    upazillas = Upazilla.objects.filter(DistrictCode_id=district_id).values('UpazillaCode', 'UpazillaName')
    return JsonResponse(list(upazillas), safe=False)

def home_view(request):
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'land_management/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'land_management/login.html')


@login_required
def index_view(request):
    today = datetime.now().date()
    two_months_from_now = today + timedelta(days=60)

    projects = Project.objects.all().annotate(total_land_area=Sum('detail__land_area_in_decimal'))


    for project in projects:
        detail_list = project.detail_set.all()
        fiscal_years = [detail.khajana_year for detail in detail_list if detail.khajana_year]
        project.near_end_flag = any(fy.end_date <= two_months_from_now and fy.end_date >= today for fy in fiscal_years)

        project.exceeded_flag = any(fy.end_date < today for fy in fiscal_years)
        total_land_count = Detail.objects.aggregate(total_land=Sum('land_area_in_decimal'))['total_land'] or 0


    context = {
        'user': request.user,
        'projects': projects,
        'total_land_count': total_land_count,
        'today':today
    }
    return render(request, 'land_management/index.html', context )


@login_required
def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    projects = Project.objects.all()
    detail_list = project.detail_set.all()
    today = datetime.now().date()
    two_months_from_now = today + timedelta(days=60)

    # Calculate fiscal year flags for each detail
    for detail in detail_list:
        fiscal_years = [detail.khajana_year for detail in detail_list if detail.khajana_year]
        # pprint.pprint(detail.__dict__)
        # print(detail.type_of_land)  # Check what is returned
        # print(detail.type_of_land.land_type if detail.type_of_land else "No Type of Land")

        if detail.khajana_year and detail.khajana_year.end_date:
            end_date = detail.khajana_year.end_date
            detail.near_end_flag = end_date <= two_months_from_now and end_date >= today
            detail.exceeded_flag = end_date < today
        else:
            detail.near_end_flag = False
            detail.exceeded_flag = False
    total_land_area = detail_list.aggregate(total_area=Sum('land_area_in_decimal'))['total_area'] or 0
    context = {
        'project': project,
        'projects': projects,
        'detail_list': detail_list,
        'total_land_area': total_land_area,
        'is_project_detail': True,
        'active_project_id': project_id,
        'today':today
    }
    return render(request, 'land_management/project_details.html', context)


@xframe_options_exempt
def download_file_view(request, pk):
    detail = get_object_or_404(Detail, pk=pk)

    if detail.mortgage_deed:
        file_path = detail.mortgage_deed.path
        try:
            return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404("File not found")
    else:
        raise Http404("No file attached")


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.db.models import Sum
# from .models import Project, Detail, Fiscal_Year
# # from .models import Project, detail, Khatian, Dag, Mortgage_Status
# from django.http import JsonResponse,FileResponse, Http404
# from django.views.decorators.clickjacking import xframe_options_exempt
#
# def home_view(request):
#     return redirect('login')
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'land_management/login.html', {'error': 'Invalid Credentials'})
#     return render(request, 'land_management/login.html')
#
#
# @login_required
# def index_view(request):
#     projects = Project.objects.all().annotate(total_land_area=Sum('detail__land_area_in_decimal'))
#     total_land_count = Detail.objects.aggregate(total_land=Sum('land_area_in_decimal'))['total_land'] or 0
#
#     return render(request, 'land_management/index.html', {
#         'user': request.user,
#         'projects': projects,
#         'total_land_count': total_land_count
#     })
# # def index_view(request):
# #     projects = Project.objects.all()
# #     total_land_count = detail.objects.aggregate(total_land=Sum('land_area_in_decimal'))['total_land'] or 0
# #     return render(request, 'land_management/index.html',
# #                   {'user': request.user, 'projects': projects, 'total_land_count': total_land_count})
#
#
# @login_required
# def project_detail_view(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     projects = Project.objects.all()
#     detail_list = project.detail_set.all()  # Fetch all detail related to the project
#     # Calculate the total land area
#     total_land_area = detail_list.aggregate(total_area=Sum('land_area_in_decimal'))['total_area'] or 0
#     context = {
#         'project': project,
#         'projects': projects,
#         'detail_list': detail_list,
#         'total_land_area': total_land_area,
#         'is_project_detail': True,
#         'active_project_id': project_id,
#     }
#     return render(request, 'land_management/project_details.html', context)
#
#
# @xframe_options_exempt
# def download_file_view(request, pk):
#     detail = get_object_or_404(Detail, pk=pk)
#
#     if detail.mortgage_deed:
#         file_path = detail.mortgage_deed.path
#         try:
#             return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#         except FileNotFoundError:
#             raise Http404("File not found")
#     else:
#         raise Http404("No file attached")
# #     project = get_object_or_404(Project, id=project_id)
# #     detail_list = project.detail_set.all()
# #     detail_with_khatians_and_dags_mortgages = []
# #     for detail in detail_list:
# #         khatians = detail.khatians.all()  # Fetch all Khatians related to this detail
# #         dags = detail.dags.all()
# #         mortgages = detail.mortgages.all()
# #
# #         detail_with_khatians_and_dags_mortgages.append({
# #             'detail': detail,
# #             'khatians': list(khatians.values('cs', 'sa', 'rs', 'bs_brs', 'city_jorip')),
# #             'dags': list(dags.values('cs', 'sa', 'rs', 'bs_brs', 'city_jorip')),  # Assuming dags has these fields
# #             'mortgages': list(mortgages.values('bank_name', 'mortgage_deed', 'poa_deeds', 'date'))
# #         })
# #
# #     context = {
# #         'project': project,
# #         'projects': Project.objects.all(),  # Fetch all projects for navigation
# #         'detail_with_khatians_and_dags_mortgages': detail_with_khatians_and_dags_mortgages,
# #         'is_project_detail': True,
# #         'active_project_id': project_id,  # To mark the current project as active
# #     }
# #     return render(request, 'land_management/project_detail.html', context)
# # detail_data = [
# #     {
# #         'sl': detail.id,
# #         'file_number': detail.file_number,
# #         'deed_number': detail.deed_number,
# #         'buyer': detail.buyer,
# #         'land_area_in_decimal': detail.land_area_in_decimal,
# #         'mouja': detail.mouja,
# #     }
# #     for detail in detail_list
# # ]
# #
# # return JsonResponse({'detail': detail_data})
#
#
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('login')
