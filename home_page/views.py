from django.shortcuts import render, redirect
from django.views import View
from allauth.account.views import SignupView
from django.contrib.auth.models import User, Permission
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


class CustomSignupView(SignupView):

    def form_valid(self, form):

        user = form.save(self.request)

        if user.profile.type == '1':
            permission = Permission.objects.get(codename='manager')
            user.user_permissions.add(permission)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = False
            user.save()
        elif user.profile.type == '2':
            permission = Permission.objects.get(codename='employee')
            user.user_permissions.add(permission)
            user.is_active = False
            user.save()

        elif user.profile.type == '3':
            permission = Permission.objects.get(codename='client')
            user.user_permissions.add(permission)
            user.is_active = False
            user.save()

        return redirect('account_signup')
