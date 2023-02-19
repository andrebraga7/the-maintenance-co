from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchVector
from client_dashboard.models import Job
from .forms import FeedbackForm
from .access import EmployeeAccessMixin


class EmployeeActiveJobs(EmployeeAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.filter(assignment=request.user)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            active_jobs = Job.objects.annotate(
                search=SearchVector(
                    'id',
                    'title',
                    'user__username',
                    'user__profile__name',
                    'user__email',
                    'description',
                    'assignment',
                ),
            ).filter(status=1).filter(search=user_query)

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

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            completed_jobs = Job.objects.annotate(
                search=SearchVector(
                    'id',
                    'title',
                    'user__username',
                    'user__profile__name',
                    'user__email',
                    'description',
                    'assignment',
                ),
            ).filter(status=2).filter(search=user_query)

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
            messages.success(request, 'Feedback added successfully.')
            return redirect('employee_active_jobs')

        else:
            messages.error(request, 'Something went wrong, form not saved.')
            return redirect('add_feedback', job_id)


class JobDone(EmployeeAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.status = 2
        job.save()
        messages.success(request, 'Job marked as done.')

        return redirect('employee_active_jobs')
