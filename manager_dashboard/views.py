from django.shortcuts import render
from django.views import View


class ManagerDashboard(View):

    def get(self, request):
        return render(request, 'dashboard_base.html')
