from django.urls import path
from .views import home_view, login_view, index_view, logout_view, project_detail_view,download_file_view
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    # path('project-details/<int:project_id>/', project_details_view, name='project_details'),
    path('project_details/<int:project_id>/', project_detail_view, name='project_details'),
    path('download/<int:pk>/', download_file_view, name='download_file'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', logout_view, name='logout'),
]
