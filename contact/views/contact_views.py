from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.db.models import Q
# from django.http import Http404


def index(request):
    contacts = models.Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_tittle': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = models.Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |   # Q permite o OU
            Q(email__icontains=search_value)     # com uso de >> | << (pipe)
            )\
        .order_by('-id')

    context = {
        'contacts': contacts,
        'site_tittle': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )


def contact(request, contact_id):
    # single_contact = models.Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        models.Contact.objects.filter(pk=contact_id, show=True)
        )

    site_tittle = f'{single_contact.first_name} {single_contact.last_name} - '

    # if single_contact is None:
    #     raise Http404()

    context = {
        'contact': single_contact,
        'site_tittle': site_tittle,
    }

    return render(
        request,
        'contact/contact.html',
        context=context
    )
