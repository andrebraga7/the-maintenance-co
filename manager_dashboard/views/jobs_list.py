from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from client_dashboard.models import Job
from ..forms import EditUserForm


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
