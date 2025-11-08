from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to the Employee Management API 👨‍💼</h2><p>Visit <a href='/api/employees/'>/api/employees/</a> to view the API endpoints.</p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
]
