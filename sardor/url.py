from django.urls import path
from .views import index_view,about_view,product_view,contact_view,testimonial_view
urlpatterns = [

path('',index_view,name = "home-page"),
path('about.html',about_view,name = "about-page"),
path('product.html',product_view,name = "product-page"),
path('contact.html',contact_view,name = "contact-page"),
path('testimonial.html',testimonial_view,name = "testimonial-page"),

]
