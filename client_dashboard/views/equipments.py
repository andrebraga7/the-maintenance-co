from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Equipment, Category
from ..forms import EquipmentForm
from .access import ClientAccessMixin


class EquipmentList(ClientAccessMixin, View):

    def get(self, request):
        equipments = Equipment.objects.filter(
            user=request.user).order_by('name')
        categories = Category.objects.filter(
            user=request.user).order_by('name')

        return render(
            request,
            'client_dashboard/equipments.html',
            {
                'equipments': equipments,
                'categories': categories,
            })


class AddEquipment(ClientAccessMixin, View):

    def get(self, request):
        return render(
            request,
            'client_dashboard/add_equipment.html',
            {'form': EquipmentForm()})

    def post(self, request):
        form = EquipmentForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('equipments')
        else:
            form = EquipmentForm()


class EditEquipment(ClientAccessMixin, View):

    def get(self, request, equipment_id):
        equipment = get_object_or_404(Equipment, id=equipment_id)
        edit_form = EquipmentForm(instance=equipment)

        return render(
            request,
            'client_dashboard/edit_equipment.html',
            {'edit_form': edit_form, })

    def post(self, request, equipment_id):
        equipment = get_object_or_404(Equipment, id=equipment_id)
        edit_form = EquipmentForm(request.POST, instance=equipment)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('equipments')
        else:
            edit_form = EquipmentForm()


class DeleteEquipment(ClientAccessMixin, View):

    def get(self, request, equipment_id):
        equipment = get_object_or_404(Equipment, id=equipment_id)
        equipment.delete()

        return redirect('equipments')
