from django.shortcuts import render

# Create your views here.


def calculator(request):
    list = ['1','2','3','+','4','5','6','-','7','8','9','*','0','.','/']
    context ={'list':list}
    return render(request,'calculator/calculator.html',context)