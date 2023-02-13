from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Permission


class Home(View):

    def get(self, request):
        return render(request, 'home_page/home.html')


class Dashboard(View):

    def get(self, request):

        if request.user.has_perm('manager_dashboard.manager'):
            return redirect('jobs_list')
        elif request.user.has_perm('manager_dashboard.client'):
            return redirect('client_jobs_list')
        elif request.user.has_perm('manager_dashboard.employee'):
            return redirect('employee_active_jobs')
        else:
            return redirect('home')
