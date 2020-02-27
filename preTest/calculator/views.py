from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from calculator.models import History
# Create your views here.
import math
def home_page(request):

    if request.POST.get('first_number', '') != '' and request.POST.get('second_number', '') != '' and request.POST.get('operator_type', '') != '' :
        
        x = float(request.POST.get('first_number',''))
        y = float(request.POST.get('second_number',''))
        operator = request.POST.get('operator_type','')

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

        return render(request,'homepage.html',{
            'calculateLists':calculateLists,
        })

    return render(request,'homepage.html')