from contact import forms
from django.shortcuts import render


def create(request):
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print()
        context = {
            'form': forms.ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': forms.ContactForm()
    }

    print()
    print(request.method)
    print()

    return render(
        request,
        'contact/create.html',
        context
    )
