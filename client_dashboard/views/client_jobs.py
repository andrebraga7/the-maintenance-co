from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.http import JsonResponse
from ..models import Job, Equipment
from ..forms import JobForm, EditJobForm
from .access import ClientAccessMixin


class NewJobs(ClientAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all().filter(user=request.user)
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            new_jobs = Job.objects.annotate(
                search=SearchVector(
                    'id',
                    'title',
                    'description',
                    'assignment',
                ),
            ).filter(status=0).filter(search=user_query)

        return render(
            request,
            'client_dashboard/new_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class ActiveJobs(ClientAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all().filter(user=request.user)
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            active_jobs = Job.objects.annotate(
                search=SearchVector(
                    'id',
                    'title',
                    'description',
                    'assignment',
                ),
            ).filter(status=1).filter(search=user_query)

        return render(
            request,
            'client_dashboard/active_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class CompletedJobs(ClientAccessMixin, View):

    def get(self, request):
        jobs = Job.objects.all().filter(user=request.user)
        new_jobs = jobs.filter(status=0)
        active_jobs = jobs.filter(status=1)
        completed_jobs = jobs.filter(status=2)

        qs = request.GET.get("queryset")

        if qs != '' and qs is not None:
            user_query = SearchQuery(qs)
            completed_jobs = Job.objects.annotate(
                search=SearchVector(
                    'id',
                    'title',
                    'description',
                    'assignment',
                ),
            ).filter(status=2).filter(search=user_query)

        return render(
            request,
            'client_dashboard/completed_jobs.html',
            {
                'new_jobs': new_jobs,
                'active_jobs': active_jobs,
                'completed_jobs': completed_jobs,
            })


class AddJob(ClientAccessMixin, View):

    def get(self, request):

        return render(
            request,
            'client_dashboard/add_job.html',
            {'form': JobForm()}
            )

    def post(self, request):
        form = JobForm(request.POST)

        if form.is_valid():
            equipment = form.instance.equipment
            category = form.instance.category
            form.instance.title = f'{equipment} in {category}'
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Form saved successfully')
            return redirect('client_new_jobs')
        else:
            messages.error(request, 'Invalid data, form not saved')
            return redirect('add_job')


class FetchEquipments(ClientAccessMixin, View):

    def get(self, request):
        category_id = request.GET.get('category_id')
        equipments = Equipment.objects.filter(category=category_id)

        return JsonResponse(list(equipments.values('id', 'name')), safe=False)


class EditJob(ClientAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = EditJobForm(instance=job)

        return render(
            request,
            'client_dashboard/edit_job.html',
            {
                'job': job,
                'edit_form': edit_form,
            })

    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        edit_form = EditJobForm(request.POST, instance=job)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Form saved successfully')
            return redirect('client_new_jobs')
        else:
            messages.error(request, 'Invalid data, form not saved')
            return redirect('client_edit_job', job_id)


class DeleteJob(ClientAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('client_new_jobs')


class RequestJobDeletion(ClientAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)

        if job.deletion:
            job.deletion = False
            job.save()
        else:
            job.deletion = True
            job.save()
        return redirect('client_active_jobs')
