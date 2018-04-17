from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def info_redirect(request):
    return redirect('info/')