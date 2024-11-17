from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import ticklist

# Create your views here.




def home(request):
    context = {'success': False}
    if request.method == "POST":
        #Handle the Form
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        due_date = request.POST['due_date']

        ins = ticklist(title = title, description = description ,status = status , due_date = due_date)
        ins.save()
        context = {'success': True}

    return render(request, "home/index.html", context)



def view_todo(request):   
    
    alltasks = ticklist.objects.all()
    context = {'tasks': alltasks}
    
    return render(request, "home/view_todo.html" , context)

def delete(request,id):   
    dele = ticklist.objects.get(id = id)
    dele.delete()
    return redirect('/view_todo')

def update(request,id):   
    mark_as_done = ticklist.objects.get(id = id)
    mark_as_done.status = 1    
    mark_as_done.save()

    return redirect('/view_todo')


# def login_page(request):
#     return HttpResponse("Login Page")