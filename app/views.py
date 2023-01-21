from django.shortcuts import render, redirect

from app.form import UserModelForm
from app.models import User


def index(request):
    users = User.objects.order_by('-created_at')
    context = {
        'users':users
    }
    return render(request, 'index.html', context)



def user_details(request, user_id):
    user = User.objects.filter(id=user_id).first()
    context = {
        'user': user
    }
    return render(request, 'user_details.html', context)



def update_user(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if request.method == 'POST':
        form = UserModelForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = UserModelForm(instance=user)
    context = {
        "form": form,
        "fullname":User.fullname,
        "image":User.image,
        "email":User.email,
        "created_at":User.created_at

    }
    return render(request, 'update-user.html', context)



def create_user(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if request.method == 'POST':
        form = UserModelForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = UserModelForm(instance=user)
    context = {
        "form": form,
        "fullname":User.fullname,
        "image":User.image,
        "email":User.email,
        "created_at":User.created_at

    }
    return render(request, 'create_user.html', context)




def delete_user(request,user_id):
    user = User.objects.filter(id=user_id).first()
    if user:
        user.delete()
        return redirect('index')
    return render(request, 'delete_user.html')