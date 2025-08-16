from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def about(request):
    """About page view"""
    return render(request, 'about.html')

def services(request):
    """Services page view"""
    return render(request, 'services.html')

def contact(request):
    """Contact page view"""
    return render(request, 'contact.html')

def consulting(request):
    """Consulting page view"""
    return render(request, 'consulting.html')

def career(request):
    """Career page view"""
    return render(request, 'career.html')

def bpo(request):
    """BPO page view"""
    return render(request, 'bpo.html')

def bpodetail(request):
    """BPO detail page view"""
    return render(request, 'bpo-detail.html')

def case(request):
    """Case page view"""
    return render(request, 'case.html')

def case_detail(request):
    """Case detail page view"""
    return render(request, 'case-detail.html')

def cultivation(request):
    """Cultivation page view"""
    return render(request, 'cultivation.html')

def product_detail(request):
    """Product detail page view"""
    return render(request, 'product-detail.html')

def company(request):
    """Company page view"""
    return render(request, 'company.html')

def recruit(request):
    """Recruit page view"""
    return render(request, 'recruit.html')