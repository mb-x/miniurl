from django.shortcuts import render, redirect, get_object_or_404
from .models import MiniURL
from .forms import MiniURLForm

# Create your views here.

def list(request):
    """ list of minified links """
    urls = MiniURL.objects.order_by("-nb_access")
    return render(request, 'list.html', locals())

def new(request):
    """ add link """
    urlForm = MiniURLForm(request.POST or None)
    if urlForm.is_valid():
        urlForm.save()
        return redirect(list)
    return render(request, 'new.html', locals())

def forword(request, code):
    """ forword url """
    url = get_object_or_404(MiniURL, code=code)
    url.nb_access += 1
    url.save()
    return redirect(url.url, permanent=True)