from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:pk>/', views.departmentApi),

    path('employee/', views.employeeApi),
    path('employee/<int:pk>/', views.employeeApi),

    path('SaveFile/', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
