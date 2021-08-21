from django.urls import path, re_path

from productapp.views import  show_products,\
    ProductDetail,product_create,ProductCreate,product_update, product_details, \
    ProductUpdate, ProductDelete, product_delete, ProductList, \
	ProductCategoryCreate


app_name = 'productapp'

urlpatterns = [
    	
	#FUNCTION BASED URLS
	#list all product names
	re_path(r'^product_list/$', ProductList.as_view(), name='show_products'),

    #path('product_list', show_products, name='show_products'),
	# list one products details
	# r'^(P<pk>\d\product_details$'

	re_path(r'^(?P<id>\d+)/product_details/', product_details, name='product_details'),
	# create a new product
	#path('create_product/', product_create, name='product_create'),
	re_path(r'^create_product/$', ProductCreate.as_view(), name='product_create'),

	#update an existing product
	#path('<int:id>/product_update', product_update, name='product_update'),
	re_path(r'^(?P<pk>\d+)/product_update/', ProductUpdate.as_view(), name='product_update'),
	#path('<int:id>/product_delete', product_delete, name='product_delete'),
	re_path(r'^(?P<pk>\d+)/product_delete/', ProductDelete.as_view(), name='product_delete'),

	# create productcategory
	re_path(r'productcategory_create', ProductCategoryCreate.as_view(), name='productcategory_create'),



	
]
