from django.shortcuts import render
from django.views import View
from ..models import Category


class Categories(View):

    def get(self, request):
        categories = Category.objects.all().filter(user=request.user)

        return render(
            request,
            'client_dashboard/categories.html',
            {'categories': categories})
