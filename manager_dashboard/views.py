from django.shortcuts import render
from django.views import View
from client_dashboard.models import Job


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
