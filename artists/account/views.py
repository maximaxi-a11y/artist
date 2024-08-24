from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View


@login_required
def dashboard(request):
    content = 'Welcome to your Dashboard'

    context = {
        'content': content,
    }
    
    return render(request, 'account/dashboard.html', context)

class CustomRegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'account/register.html'  # Replace with your registration template

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Replace 'home' with your desired redirect URL name
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # Replace with your login template

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Replace 'home' with your desired redirect URL name
        return super().dispatch(request, *args, **kwargs)
