from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from ..models import Job, Equipment
from ..forms import JobForm, EditJobForm
from .access import ClientAccessMixin


class ClientJobsList(ClientAccessMixin, View):

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
            return redirect('client_jobs_list')


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

            return redirect('client_jobs_list')


class DeleteJob(ClientAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        job.delete()
        return redirect('client_jobs_list')


class RequestJobDeletion(ClientAccessMixin, View):

    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)

        if job.deletion:
            job.deletion = False
            job.save()
        else:
            job.deletion = True
            job.save()
        return redirect('client_jobs_list')
