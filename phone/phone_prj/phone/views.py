from django.shortcuts import render
from .models import Phone

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'phone/list.html', {'phones' : phones})

def result(request):
    keyword = request.GET.get('keyword')
    
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')
    
    context = {
        'phones' : phones,
        'keyword' : keyword
    }
    
    return render(request, 'phone/result.html', context)
