from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import MiniURL
from .forms import MiniURLForm
from .models import Article, Eleve
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

class ListArticles(ListView):
    Eleve(nom="Mathieu", moyenne=18).save()
    Eleve(nom="Maxime", moyenne=7).save()  # Le vilain petit canard !
    Eleve(nom="Bastien", moyenne=10).save()
    Eleve(nom="Sofiane", moyenne=10).save()

    model = Article
    context_object_name = "articles"
    template_name = "blog/accueil.html"
    paginate_by=5

def list(request):
    """ list of minified links """
    urls_list = MiniURL.objects.order_by("-nb_access")
    page = request.GET.get('page', 1)
    paginator = Paginator(urls_list, 1)
    try:
        urls = paginator.page(page)
    except:
        urls = paginator.page(paginator.num_pages)

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