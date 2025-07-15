from django.contrib import auth, messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from expense_tracker.forms import ExpenseForm
from expense_tracker.models import Profile, Expenses


def home(request):
    expenses = Expenses.objects.filter(user__username=request.user.username)

    context = {
        "expenses": expenses
    }

    return render(request, 'home.html', context=context)

def profile(request):
    user = get_object_or_404(User, id=request.user.id)

    context = {
        'user': user,
    }

    return render(request, 'profile.html', context=context)

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    context = {'form': form}

    return render(request, 'add_expense.html', context=context)

def delete(request, eid):
    expense_obj =get_object_or_404(Expenses, id=eid)
    expense_obj.delete()
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        auth.logout(request)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return None
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Email already registered.')
            return None
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    return None