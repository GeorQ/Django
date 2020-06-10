from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = product.review_set.all()
    p_name = 'review_of_' + str(pk)
    form = ReviewForm
    if reviews.count():
        is_review_exist = True
    else:
        is_review_exist = False
    if request.method == 'POST':
        if request.session.get(p_name, 0) < 1:
            form = ReviewForm(request.POST)
            if form.is_valid():
                Review.objects.create(text=form.cleaned_data['text'], product=product)
                num = request.session.get(p_name, 0)
                request.session[p_name] = num + 1
                is_review_exist = True
                form = ReviewForm
    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist,
    }
    print(request.session.get(p_name, 'kek'))
    # request.session[p_name] = 0
    return render(request, template, context)
