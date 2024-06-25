from django.shortcuts import render

def index_view(request):
    return render(request,"index.html")

def about_view(request):
    return render(request,"about.html")

def product_view(request):
    return render(request,"product.html")

def contact_view(request):
    return render(request,"contact.html")

def testimonial_view(request):
    return render(request,"testimonial.html")