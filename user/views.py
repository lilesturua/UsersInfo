from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm


def create_user(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("user list")
    return render(request, "create_user.html", {'form':form})


def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {'users':users})


def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            return redirect("user list")
    return render(request, "update_user.html", {'form':form})


def delete_user(request, user_id):
    member = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        member.delete()

        return redirect("user list")
    return render(request, 'delete_user.html', {"member":member})



