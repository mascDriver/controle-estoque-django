from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from venda.views import return_grapf


@login_required
def home(request):
    return render(request, "home.html", return_grapf())
