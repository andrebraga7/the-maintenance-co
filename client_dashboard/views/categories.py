from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Category
from ..forms import AddCategoryForm


class Categories(View):

    def get(self, request):
        categories = Category.objects.all().filter(user=request.user)

        return render(
            request,
            'client_dashboard/categories.html',
            {
                'categories': categories,
                'form': AddCategoryForm(),
            })

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('categories')


class DeleteCategory(View):

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('categories')
