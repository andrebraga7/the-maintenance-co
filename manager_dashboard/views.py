from django.shortcuts import render, redirect
from django.views import View
from client_dashboard.models import Job
from allauth.account.views import SignupView
from django.contrib.auth.models import User, Permission


class NewJobs(View):

    def get(self, request):
        jobs = Job.objects.filter(status=0)

        return render(
            request,
            'manager_dashboard/new_jobs.html',
            {'jobs': jobs})


class ActiveJobs(View):

    def get(self, request):
        jobs = Job.objects.filter(status=1)

        return render(
            request,
            'manager_dashboard/active_jobs.html',
            {'jobs': jobs})


class CompletedJobs(View):

    def get(self, request):
        jobs = Job.objects.filter(status=2)

        return render(
            request,
            'manager_dashboard/completed_jobs.html',
            {'jobs': jobs})


class ShowUsers(View):

    def get(self, request):
        users = User.objects.all()

        return render(
            request,
            'manager_dashboard/show_users.html',
            {'users': users})


class CustomSignupView(SignupView):

    def form_valid(self, form):

        user = form.save(self.request)

        if user.profile.type == 'manager':
            permission = Permission.objects.get(codename='manager')
            user.user_permissions.add(permission)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        elif user.profile.type == 'employee':
            permission = Permission.objects.get(codename='employee')
            user.user_permissions.add(permission)
        elif user.profile.type == 'client':
            permission = Permission.objects.get(codename='client')
            user.user_permissions.add(permission)

        return redirect('dashboard')
