from django.shortcuts import render, HttpResponse
from .models import Phone

def show_catalog(request):
    type = request.GET.get("sort")
    if (type == "incr"):
        template = 'catalog.html'
        phones = Phone.objects.all().order_by("price")
        context = {'phones': phones}
        return render(request, template, context)
    elif (type == "decr"):
        template = 'catalog.html'
        phones = Phone.objects.all().order_by("-price")
        context = {'phones': phones}
        return render(request, template, context)
    elif (type == "decr"):
        template = 'catalog.html'
        phones = Phone.objects.all().order_by("model")
        context = {'phones': phones}
        return render(request, template, context)
    else:
        template = 'catalog.html'
        phones = Phone.objects.all()
        context = {'phones': phones}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__iexact=slug)
    context = {'phone': phone}
    return render(request, template, context)
