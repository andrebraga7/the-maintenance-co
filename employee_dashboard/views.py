from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from client_dashboard.models import Job
from .forms import FeedbackForm
from .access import EmployeeAccessMixin


class EmployeeActiveJobs(EmployeeAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.filter(assignment=request.user)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'employee_dashboard/employee_active_jobs.html',
            {
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class EmployeeCompletedJobs(EmployeeAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.filter(assignment=request.user)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        return render(
            request,
            'employee_dashboard/employee_completed_jobs.html',
            {
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class AddFeedback(EmployeeAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        feedback_form = FeedbackForm(instance=job)

        return render(
            request,
            'employee_dashboard/add_feedback.html',
            {
                'job': job,
                'feedback_form': feedback_form,
            })

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        feedback_form = FeedbackForm(request.POST, instance=job)

        if feedback_form.is_valid():
            feedback_form.save()
            return redirect('employee_active_jobs')


class JobDone(EmployeeAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.status = 2
        job.save()

        return redirect('employee_active_jobs')
