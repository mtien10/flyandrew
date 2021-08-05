import json
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


@login_required
def index(request):
    return render(request, 'index.html')


# Category
def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'staff/category/form.html'
    success_url = '/staff'


def deleteCategory(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            c = Category.objects.get(pk=pk)
            c.delete()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'

    result = {'success': success, 'errors': error}
    return HttpResponse(json.dumps(result), content_type='application/json')


# Product
def listProduct(request):
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request, 'staff/product/list.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'staff/product/form.html'
    success_url = '/staff/list-product'


def deleteProduct(request, pk):
    error = ''
    success = False
    if request.method == 'POST':
        try:
            p = Product.objects.get(pk=pk)
            p.delete()
            success = True
        except Exception as e:
            error = str(e)
    else:
        error = 'Method not allow'

    result = {'success': success, 'errors': error}
    return HttpResponse(json.dumps(result), content_type='application/json')


# Order
def listOrder(request):
    return render(request, 'staff/order/list.html')


def viewOrder(request, pk):
    return render(request, 'staff/order/view_detail.html')
