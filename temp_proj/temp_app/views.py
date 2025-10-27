from django.shortcuts import render
from django.http import HttpResponse

def helloooooooo(request):
    return HttpResponse('hiiiiiiiiii')

def info(request):
    my_context={
        'name' : 'Davit',
        'lastname' :'Bagauri',
        'nickname' : 'baga',
        'age': 17,
    }
    return render(request,'info.html',context=my_context)

def hobby(request):
    hobby_list=['gym','cycling','gaming','coding']
    my_hobby={
        'hobbies' : hobby_list,
        'grade': 12,
    }
    return render(request,'hobbies.html',context=my_hobby)

