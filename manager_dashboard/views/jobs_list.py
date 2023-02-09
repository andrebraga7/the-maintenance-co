from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from client_dashboard.models import Job
from ..forms import AssignJobForm
from client_dashboard.forms import JobForm


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
                'assign_form':  AssignJobForm(),
            })


class EditJob(View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = JobForm(instance=job)

        return render(
            request,
            'manager_dashboard/edit_job.html',
            {'edit_form': edit_form}
            )

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = JobForm(request.POST, instance=job)

        if edit_form.is_valid():
            equipment = edit_form.instance.equipment
            category = edit_form.instance.category
            edit_form.instance.title = f'{equipment} in {category}'
            edit_form.save()

            return redirect('jobs_list')


class AssignJob(View):

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        assign_form = AssignJobForm(request.POST, instance=job)

        if assign_form.is_valid():
            assign_form.instance.status = 1
            assign_form.save()
            return redirect('jobs_list')


class ManagerDeleteJob(View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('jobs_list')
