from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Mouth
from . import forms


def ask_odontogram(request):
    return render(request, 'ask_odontogram.html')


def new_odontogram(request):
    odontogram = Mouth.objects.create()
    # append odontogram to profile
    if request.method == 'POST':
        return redirect('record:tooth', pk_mouth=odontogram.id)
    return render(request, 'odontogram.html', {
        'odontogram': odontogram,
        }
    )


def tooth_view(request, pk_mouth, nb_tooth):
    odontogram = Mouth.objects.get(pk=pk_mouth)
    tooth_form = forms.T11Form(instance=odontogram)
    if request.method == 'POST':
        tooth_form = forms.T11Form(request.POST, instance=odontogram)
        if tooth_form.is_valid():
            # append to profile
            tooth_form.save()
            messages.success(request,'Estado del diente actualizado!')
            return redirect('record:update_odontogram', pk_mouth=pk_mouth)
    return render(request, 'tooth.html', {
        'tooth_form': tooth_form,
        'pk_mouth': pk_mouth,
        }
    )


def update_odonto(request, pk_mouth):
    odontogram = Mouth.objects.get(pk=pk_mouth)
    print(pk_mouth)
    if request.method == 'POST':
        return redirect('record:tooth', pk_mouth=pk_mouth)
    return render(request, 'odontogram.html', {
        'odontogram': odontogram,
        'pk_mouth': pk_mouth,
        }
    )
