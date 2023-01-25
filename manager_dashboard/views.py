from django.shortcuts import render
from django.views import View
from client_dashboard.models import Job


class Initial(View):

    def get(self, request):
        jobs = Job.objects.all()

        return render(request, 'manager_dashboard/initial.html', {'jobs': jobs})
