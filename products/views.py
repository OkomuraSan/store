from django.shortcuts import render
from products.models import prod, prodCategory

def index(request):
    context = {
        "title":"Home page"
               }
    return render(request, "products/index.html ", context)


def products(request):
    context = {
        "title": "Product page",
        "products": prod.objects.all(),
        "category": prodCategory.objects.all(),

    }
    return render(request, "products/products.html ", context)