# views.py

from django.shortcuts import render
from .models import Users

def user_data_view(request):
    users_data = Users.objects.values('sub_sr', 'password')
    return render(request, 'templates.html', {'users_data': users_data})
