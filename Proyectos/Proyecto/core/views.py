from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from . import models
from django.urls import reverse_lazy
from .models import InfoRequest

# Create your views here.
def about(request):
    return render(request, 'core/about.html')

@login_required
def home(request):
    comentarios = InfoRequest.objects.all()
    return render(request, 'core/home.html', {'comentarios': comentarios})

@login_required
def products(request):
    return render(request, 'core/products.html')

@login_required
def base(request):
    return render(request, 'core/base.html')



def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', data)

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'core/comentario.html'
    model = models.InfoRequest
    fields = ['tema', 'descripcion']
    success_url = reverse_lazy('home')
    success_message = 'Gracias por realizar un comentario, se ha añadido al foro!'

    def form_valid(self, form):
        # Set the current user as the usuario field
        form.instance.usuario = self.request.user.username
        return super().form_valid(form)
