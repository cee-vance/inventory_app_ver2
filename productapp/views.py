from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views import View

from .models import Product
from productapp.forms import *


def show_products(request):
    prod_lst = Product.objects.all()
    template = loader.get_template('productapp/product_list.html')
    context = {
        'prod_lst': prod_lst
    }
    return HttpResponse(template.render(context,request))

# function based single product details
def product_details(request, id):
    prod = get_object_or_404(Product, pk = int(id))
    return render(request , 'productapp/product_detail.html',{'product':prod})

# class based product details
class ProductDetail(DetailView):
    model = Product
    template = 'productapp/product_detail.html'
    context_object_name = 'prod'



# create a new product
def product_create(request):
    # request is get
    if request.method == 'GET':
        form = ProductForm
        return render(request, 'productapp/product_create.html',{'product_form':form})
    # otherwise post
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # show the user all the products including added one
            return HttpResponseRedirect(reverse('productapp:show_products'))
        else:
            return render(request, 'productapp/product_create.html', {'product_form' : form})


# class based create
"""
class ProductCreate(View):
    def get(self,request):
        form = ProductForm
        return render(request, 'productapp/product_create.html', {'product_form':form})

    def post(self,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productapp:show_products'))
        else:
            return render(request, 'productapp/product_create.html', {'product_form':form})
"""




def product_update(request , id ):
    product = get_object_or_404(Product, id=id) # already exists
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'GET':
        return render(request , 'productapp/product_update.html', {'product_form': form})
    else: # POST
        
        if form.is_valid():  #
            form.save(commit=True)  # insert
            return HttpResponseRedirect(reverse('productapp:show_products'))  # domian name/blogs/ # blog:list_blogs
        else:
            return render(request, 'productapp/product_update.html', {'product_form': form})

# CreateView
class ProductCreate(CreateView):
    model = Product
    # form_class = BlogForm
    fields = '__all__'
    template_name = 'productapp/product_create.html'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('productapp:show_products') # reverse map a url -

# class based update
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'productapp/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('productapp:show_products')
    context_object_name = 'prod'


# function based delete
# doesn't work
def product_delete(request, id):
    prod = get_object_or_404(Product, pk=id)

    if request.method == 'POST' and request.user.is_authenticated :
        name = prod.name
        prod.delete()
        template = 'productapp/product_delete.html'
        return HttpResponse( template.render( {'product':name}, request))
    
    

class ProductDelete(DeleteView):
    # specify the model you want to use
    model = Product

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = '~productapp/list_products'
	

class ProductList(ListView):
    template_name = 'productapp/product_list.html'
    model = Product    # queryset = Blog.objects.filter(text='ABC')
    context_object_name = 'prod_lst' #'blogs' 'objects_list [{}.{}.{}]