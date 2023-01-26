from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Permission


class Home(View):

    def get(self, request):
        return render(request, 'home_page/home.html')


class Dashboard(View):

    def get(self, request):

        if request.user.has_perm('client_dashboard.is_manager'):
            return redirect('manager')
        else:
            return redirect('home')
