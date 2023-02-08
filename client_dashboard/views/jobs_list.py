from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from ..models import Job, Equipment
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
            equipment = form.instance.equipment
            category = form.instance.category
            form.instance.title = f'{equipment} in {category}'
            form.instance.user = request.user
            form.save()
            return redirect('client_jobs_list')


class FetchEquipments(View):

    def get(self, request):
        category_id = request.GET.get('category_id')
        equipments = Equipment.objects.filter(category=category_id)

        return JsonResponse(list(equipments.values('id', 'name')), safe=False)


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
            equipment = edit_form.instance.equipment
            category = edit_form.instance.category
            edit_form.instance.title = f'{equipment} in {category}'
            edit_form.save()

            return redirect('client_jobs_list')
