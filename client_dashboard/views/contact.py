from django.shortcuts import render
from django.views import View
from ..forms import ContactForm


class Contact(View):

    def get(self, request):
        return render(
            request,
            'client_dashboard/contact.html',
            {'form': ContactForm()})
