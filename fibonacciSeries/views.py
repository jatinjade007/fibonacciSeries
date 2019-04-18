from django.shortcuts import render
from django.shortcuts import HttpResponse


from .forms import *
from django.http import HttpResponseRedirect
import time

# Create your views here.
def index(request):
    if request.method=='GET':
        start = time.clock()
        form1=inputform(request.GET)
        if form1.is_valid():
            nterms = form1.cleaned_data['number']

            # first two terms
            n1 = 1
            n2 = 1
            count = 0

            # check if the number of terms is valid
            if nterms <= 0:
                result = 'Output: Please enter a positive integer.'
            elif nterms == 1:
                series = '['+str(n1)+']'
                result = 'Output: '+series+'.'
            else:
                series = '['
                while count < nterms:
                    series = series+str(n1)+','
                    nth = n1 + n2
                    # update values
                    n1 = n2
                    n2 = nth
                    count += 1
                series = series+']'
                result = 'Output: '+series+'.'
            totalTimeTaken = 'Time taken to get result: '+str(time.clock() - start)
            #return HttpResponseRedirect('index.html')
            return HttpResponse(result+'<br>'+totalTimeTaken)
        else:
            form1 = inputform()
            return render(request, 'fibonacciSeries/index.html', {'frm':form1})
    else:
          return render(request, 'fibonacciSeries/index.html')
