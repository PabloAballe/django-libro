from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .forms import *

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('home')
    else:
        form = ContactoForm()
    context={'form': form}
    return render(request, 'contacto.html',context)
