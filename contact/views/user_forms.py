from django.shortcuts import render
from contact import forms


def register(request):
    form = forms.RegisterForm

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
