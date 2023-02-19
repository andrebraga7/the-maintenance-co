from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib.auth.models import User, Permission
from ..forms import EditUserForm, EditProfileForm
from .access import ManagerAccessMixin


class ShowUsers(ManagerAccessMixin, View):

    def get(self, request):
        users = User.objects.all().order_by('profile__name')

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            users = User.objects.annotate(
                search=SearchVector(
                    'id',
                    'username',
                    'profile__name',
                    'profile__type',
                    'email',
                ),
            ).filter(search=user_query).order_by('profile__name')

        return render(
            request,
            'manager_dashboard/show_users.html',
            {'users': users}
            )


class ApproveUser(ManagerAccessMixin, View):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.is_active = True
        user.save()
        
        messages.success(request, 'User approved.')

        return redirect('show_users')


class EditUser(ManagerAccessMixin, View):

    def get(self, request, user_id, *args, **kwargs):
        edit_user = get_object_or_404(User, id=user_id)
        form1 = EditProfileForm(instance=edit_user.profile)
        form2 = EditUserForm(instance=edit_user)

        return render(
            request,
            'manager_dashboard/edit_user.html',
            {
                'form1': form1,
                'form2': form2,
            })

    def post(self, request, user_id, *args, **kwargs):
        edit_user = get_object_or_404(User, id=user_id)
        form1 = EditProfileForm(request.POST, instance=edit_user.profile)
        form2 = EditUserForm(request.POST, instance=edit_user)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, 'User edited successfully.')
        else:
            messages.error(request, 'Something went wrong, form not saved.')

        return redirect('show_users')


class DeleteUser(ManagerAccessMixin, View):

    def get(self, request, user_id):
        delete_user = get_object_or_404(User, id=user_id)
        delete_user.delete()
        messages.success(request, 'User deleted successfully.')   
        return redirect('show_users')
