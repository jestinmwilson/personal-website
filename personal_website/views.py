from django.shortcuts import render, redirect
from .forms import ConatactMeForm
from django.contrib import messages
# from django.core.mail import send_mail


def about_me(request):
    return render(request, "about.html", {})


def resume(request):
    return render(request, "resume.html", {})


def contact_me(request):
    if request.method == 'POST':
        form = ConatactMeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail('jestinmwilson-Form', cd['message'],
            #           'mail.jestinmwilson.com', ['jestinmwill@gmail.com.com', ])
            messages.success(request, 'Your message has been successfully sent')
            return redirect('contact-me')
    else:
        form = ConatactMeForm()

    context = {
        'form': form,
    }
    return render(request, "contact-me.html", context)
