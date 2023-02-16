from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from ..models import Category
from ..forms import CategoryForm
from .access import ClientAccessMixin


class Categories(ClientAccessMixin, View):

    def get(self, request):
        categories = Category.objects.all().filter(
            user=request.user).order_by('name')

        return render(
            request,
            'client_dashboard/categories.html',
            {
                'categories': categories,
                'form': CategoryForm(),
            })

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Form saved successfully')
        else:
            messages.error(request, 'Invalid data, form not saved')

        return redirect('categories')


class EditCategory(ClientAccessMixin, View):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        edit_form = CategoryForm(instance=category)

        return render(
            request,
            'client_dashboard/edit_category.html',
            {
                'category': category,
                'edit_form': edit_form,
            })

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, 'Form saved successfully')
            return redirect('categories')

        else:
            messages.error(request, 'Invalid data, form not saved')
            return redirect('edit_category', category_id)


class DeleteCategory(ClientAccessMixin, View):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('categories')
