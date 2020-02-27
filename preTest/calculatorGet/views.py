from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from calculator.models import History
# Create your views here.
import math
def home_pageGet(request):

    if request.GET.get('first_number', '') != '' and request.GET.get('second_number', '') != '' and request.GET.get('operator_type', '') != '' :
        
        x = float(request.GET.get('first_number',''))
        y = float(request.GET.get('second_number',''))
        operator = request.GET.get('operator_type','')

        result = 0
        result = x+y if operator == '+' else result
        result = x-y if operator == '-' else result
        result = x*y if operator == '*' else result
        result = x/y if operator == '/' else result
        result = x%y if operator == '%' else result
        result = x**y if operator == '**' else result
        result = math.sqrt(x) if operator == 'sqrt' else result
    
        History.objects.create(expression= str(x)+operator+str(y),answer = str(result))
        calculateLists = History.objects.all()

        return render(request,'homepageGet.html',{
            'calculateLists':calculateLists,
        })

    return render(request,'homepageGet.html')