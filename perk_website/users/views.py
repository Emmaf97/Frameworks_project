from django.shortcuts import render,redirect
from django.contrib import messages #import for messages
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}, now you can login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        # print(form.fields)
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')
   
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            # Save user form
            u_form.save()

            # Save profile form
            profile = p_form.save(commit=False)
            
            # Handle predefined image choices
            selected_image = p_form.cleaned_data.get('image_choice')
            if selected_image:
                # This is a relative path to a static file, not an actual file object
                # To use static files, ensure it is served correctly
                profile.image = selected_image
            else:
                # Handle file upload (if provided)
                if 'image' in request.FILES:
                    profile.image = request.FILES['image']
            
            profile.save()  # Save profile with updated image
            
            messages.success(request, 'Your account has been successfully updated.')
            return redirect('thread-thread')  # Ensure this is a valid URL name

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
      
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')