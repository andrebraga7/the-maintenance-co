from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from client_dashboard.models import Job
from allauth.account.views import SignupView
from django.contrib.auth.models import User, Permission
from .forms import EditUserForm, EditProfileForm


class CustomSignupView(SignupView):

    def form_valid(self, form):

        user = form.save(self.request)

        if user.profile.type == '1':
            permission = Permission.objects.get(codename='manager')
            user.user_permissions.add(permission)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        elif user.profile.type == '2':
            permission = Permission.objects.get(codename='employee')
            user.user_permissions.add(permission)
        elif user.profile.type == '3':
            permission = Permission.objects.get(codename='client')
            user.user_permissions.add(permission)

        return redirect('account_signup')


class JobsList(View):

    def get(self, request):
        jobs = Job.objects.all()
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'manager_dashboard/jobs_list.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class ShowUsers(View):

    def get(self, request):
        users = User.objects.all().filter(
            profile__name__isnull=False).order_by('profile__name')

        return render(
            request,
            'manager_dashboard/show_users.html',
            {'users': users}
            )


class EditUser(View):

    def get(self, request, user_id, *args, **kwargs):
        edit_user = get_object_or_404(User, id=user_id)
        form1 = EditUserForm(instance=edit_user)
        form2 = EditProfileForm(instance=edit_user.profile)

        return render(
            request,
            'manager_dashboard/edit_user.html',
            {
                'form1': form1,
                'form2': form2,
            })
