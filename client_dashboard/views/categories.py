from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Category
from ..forms import CategoryForm


class Categories(View):

    def get(self, request):
        categories = Category.objects.all().filter(user=request.user)

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
            return redirect('categories')
        else:
            form = CategoryForm()


class EditCategory(View):

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
            return redirect('categories')
        else:
            form = CategoryForm()


class DeleteCategory(View):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('categories')
