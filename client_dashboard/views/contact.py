from django.shortcuts import render
from django.views import View
from ..forms import ContactForm
from .access import ClientAccessMixin


class Contact(ClientAccessMixin, View):

    def get(self, request):
        email = request.user.email
        data = {'email': email}

        return render(
            request,
            'client_dashboard/contact.html',
            {'form': ContactForm(initial=data)})
