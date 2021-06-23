from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html', {})


@login_required
def private_view(request):
    # if not request.user.is_authenticated:
    #     return redirect(settings.LOGIN_URL)
    #
    return render(request, 'private_view.html', {})


