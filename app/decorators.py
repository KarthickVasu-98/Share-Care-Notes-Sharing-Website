from django.http import HttpResponse
from django.shortcuts import redirect,render


def unauthenticates_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'app/home.htm')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')    
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group =None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'students':
            return render (request, 'app/home.htm')

        if group == 'teachers':
            return render (request, 'app/teacher.htm')

    return wrapper_func







