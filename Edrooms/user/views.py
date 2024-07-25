from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user=form.save()
             login(request,user)
             return redirect('classroom:classroom_list')
    
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', { 'form': form })



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', 'classroom:classroom_list')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, 'user/login.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')  

