from django.shortcuts import render,redirect
from django.contrib import messages #import for messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}, now you can login.')
            return redirect('thread-home')
    else:
        form = UserRegisterForm()
        # print(form.fields)
    return render(request, 'users/register.html', {'form': form})