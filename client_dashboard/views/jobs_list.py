from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Job
from ..forms import JobForm


class ClientJobsList(View):

    def get(self, request):
        jobs = Job.objects.all().filter(user=request.user)
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'client_dashboard/client_jobs_list.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class AddJob(View):

    def get(self, request):

        return render(
            request,
            'client_dashboard/add_job.html',
            {'form': JobForm()}
            )

    def post(self, request):
        form = JobForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('client_jobs_list')


class EditJob(View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = JobForm(instance=job)

        return render(
            request,
            'client_dashboard/edit_job.html',
            {'edit_form': edit_form}
            )

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = JobForm(request.POST, instance=job)

        if edit_form.is_valid():
            edit_form.save()

            return redirect('client_jobs_list')
