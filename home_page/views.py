from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from allauth.account.views import SignupView
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from client_dashboard.forms import ContactForm
from .forms import HomeUserForm, HomeProfileForm


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

    def post(View):
        messages.success(request, 'Message sent successfully!')
        return redirect('home_contact')


class AwaitingApproval(View):

    def get(self, request):
        return render(request, 'home_page/awaiting_approval.html')


class EditAccount(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        edit_user = get_object_or_404(User, id=request.user.id)
        form1 = HomeProfileForm(instance=edit_user.profile)
        form2 = HomeUserForm(instance=edit_user)

        return render(
            request,
            'home_page/edit_account.html',
            {
                'form1': form1,
                'form2': form2,
            })

    def post(self, request, *args, **kwargs):
        edit_user = get_object_or_404(User, id=request.user.id)
        form1 = HomeProfileForm(request.POST, instance=edit_user.profile)
        form2 = HomeUserForm(request.POST, instance=edit_user)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, 'Account edited successfully.')
        else:
            messages.error(request, 'Something went wrong, form not saved.')

        return redirect('dashboard')


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


class CustomSignupView(SignupView, View):

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

        messages.success(self.request, 'User created successfully.')

        return redirect('account_signup')
