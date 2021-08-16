from django.shortcuts import render

# Create your views here.

task=['make projects','learn django','make new projects again']

def index(request):
    if request.method == 'POST':
        data=request.POST.get('task')
        task.append(data)
    else:
        return render(request,"tasks/index.html",{
        "tasks":task
    })


    return render(request,"tasks/index.html",{
        "tasks":task
    })
