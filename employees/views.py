from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# ✅ List + Create employees
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# ✅ Retrieve + Update + Delete individual employee
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
