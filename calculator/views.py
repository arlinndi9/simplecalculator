from django.shortcuts import render

# Create your views here.
def index(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        if 'add' in request.POST:
            result = num1 + num2
        elif 'sub' in request.POST:
            result = num1 - num2
        elif 'mul' in request.POST:
            result = num1 * num2
        elif 'div' in request.POST:
            if num2 != 0:
                result = num1 / num2
        context = {
            'result': result,
            'num1': num1,
            'num2': num2
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

    context = {'result': result,
               'num1':num1,
               'num2':num2}
    return render(request, 'index.html',context)