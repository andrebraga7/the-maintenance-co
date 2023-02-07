from django.shortcuts import render, redirect
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
