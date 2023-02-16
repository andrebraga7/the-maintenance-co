from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Permission
from client_dashboard.forms import ContactForm


class Home(View):

    def get(self, request):
        return render(request, 'home_page/home.html')


class About(View):

    def get(self, request):
        return render(request, 'home_page/about.html')


class Contact(View):

    def get(self, request):
        return render(
            request,
            'home_page/contact.html',
            {'form': ContactForm()})


class Dashboard(View):

    def get(self, request):

        if request.user.has_perm('manager_dashboard.manager'):
            return redirect('new_jobs')
        elif request.user.has_perm('manager_dashboard.client'):
            return redirect('client_new_jobs')
        elif request.user.has_perm('manager_dashboard.employee'):
            return redirect('employee_active_jobs')
        else:
            return redirect('home')
