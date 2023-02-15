from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from client_dashboard.models import Job
from ..forms import AssignJobForm, EditJobForm
from .access import ManagerAccessMixin


class NewJobs(ManagerAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all()
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'manager_dashboard/new_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
                'assign_form':  AssignJobForm(),
            })


class ActiveJobs(ManagerAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all()
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'manager_dashboard/active_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
                'assign_form':  AssignJobForm(),
            })


class CompletedJobs(ManagerAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all()
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'manager_dashboard/completed_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class EditJob(ManagerAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = EditJobForm(instance=job)

        return render(
            request,
            'manager_dashboard/edit_job.html',
            {
                'job': job,
                'edit_form': edit_form
            })

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = EditJobForm(request.POST, instance=job)

        if edit_form.is_valid():
            equipment = edit_form.instance.equipment
            category = edit_form.instance.category
            edit_form.instance.title = f'{equipment} in {category}'
            edit_form.save()

            return redirect('active_jobs')


class AssignJob(ManagerAccessMixin, View):

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        assign_form = AssignJobForm(request.POST, instance=job)

        if assign_form.is_valid():
            assign_form.instance.status = 1
            assign_form.save()
            return redirect('active_jobs')


class ManagerDeleteJob(ManagerAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('new_jobs')


class CancelDeletion(ManagerAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.deletion = False
        job.save()
        return redirect('active_jobs')


class JobDone(ManagerAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)

        if job.status == 1:
            job.status = 2
            job.save()
        else:
            job.status = 1
            job.save()

        return redirect('active_jobs')
