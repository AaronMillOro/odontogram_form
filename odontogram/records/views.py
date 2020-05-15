import ast
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
    nb_tooth
    odontogram = Mouth.objects.get(pk=pk_mouth)
    # Selection of field
    if nb_tooth == 't_11':
        tooth_form = forms.T11Form(instance=odontogram)
    elif nb_tooth == 't_12':
        tooth_form = forms.T12Form(instance=odontogram)
    elif nb_tooth == 't_13':
        tooth_form = forms.T13Form(instance=odontogram)
    elif nb_tooth == 't_14':
        tooth_form = forms.T14Form(instance=odontogram)
    elif nb_tooth == 't_15':
        tooth_form = forms.T15Form(instance=odontogram)
    elif nb_tooth == 't_16':
        tooth_form = forms.T16Form(instance=odontogram)
    elif nb_tooth == 't_17':
        tooth_form = forms.T17Form(instance=odontogram)
    elif nb_tooth == 't_18':
        tooth_form = forms.T18Form(instance=odontogram)
    elif nb_tooth == 't_21':
        tooth_form = forms.T21Form(instance=odontogram)
    elif nb_tooth == 't_22':
        tooth_form = forms.T22Form(instance=odontogram)
    elif nb_tooth == 't_23':
        tooth_form = forms.T23Form(instance=odontogram)
    elif nb_tooth == 't_24':
        tooth_form = forms.T24Form(instance=odontogram)
    elif nb_tooth == 't_25':
        tooth_form = forms.T25Form(instance=odontogram)
    elif nb_tooth == 't_26':
        tooth_form = forms.T26Form(instance=odontogram)
    elif nb_tooth == 't_27':
        tooth_form = forms.T27Form(instance=odontogram)
    elif nb_tooth == 't_28':
        tooth_form = forms.T28Form(instance=odontogram)
    elif nb_tooth == 't_31':
        tooth_form = forms.T31Form(instance=odontogram)
    elif nb_tooth == 't_32':
        tooth_form = forms.T32Form(instance=odontogram)
    elif nb_tooth == 't_33':
        tooth_form = forms.T33Form(instance=odontogram)
    elif nb_tooth == 't_34':
        tooth_form = forms.T34Form(instance=odontogram)
    elif nb_tooth == 't_35':
        tooth_form = forms.T35Form(instance=odontogram)
    elif nb_tooth == 't_36':
        tooth_form = forms.T36Form(instance=odontogram)
    elif nb_tooth == 't_37':
        tooth_form = forms.T37Form(instance=odontogram)
    elif nb_tooth == 't_38':
        tooth_form = forms.T38Form(instance=odontogram)
    elif nb_tooth == 't_41':
        tooth_form = forms.T41Form(instance=odontogram)
    elif nb_tooth == 't_42':
        tooth_form = forms.T42Form(instance=odontogram)
    elif nb_tooth == 't_43':
        tooth_form = forms.T43Form(instance=odontogram)
    elif nb_tooth == 't_44':
        tooth_form = forms.T44Form(instance=odontogram)
    elif nb_tooth == 't_45':
        tooth_form = forms.T45Form(instance=odontogram)
    elif nb_tooth == 't_46':
        tooth_form = forms.T46Form(instance=odontogram)
    elif nb_tooth == 't_47':
        tooth_form = forms.T47Form(instance=odontogram)
    elif nb_tooth == 't_48':
        tooth_form = forms.T48Form(instance=odontogram)
    elif nb_tooth == 't_51':
        tooth_form = forms.T51Form(instance=odontogram)
    elif nb_tooth == 't_52':
        tooth_form = forms.T52Form(instance=odontogram)
    elif nb_tooth == 't_53':
        tooth_form = forms.T53Form(instance=odontogram)
    elif nb_tooth == 't_54':
        tooth_form = forms.T54Form(instance=odontogram)
    elif nb_tooth == 't_55':
        tooth_form = forms.T55Form(instance=odontogram)
    elif nb_tooth == 't_61':
        tooth_form = forms.T61Form(instance=odontogram)
    elif nb_tooth == 't_62':
        tooth_form = forms.T62Form(instance=odontogram)
    elif nb_tooth == 't_63':
        tooth_form = forms.T63Form(instance=odontogram)
    elif nb_tooth == 't_64':
        tooth_form = forms.T64Form(instance=odontogram)
    elif nb_tooth == 't_65':
        tooth_form = forms.T65Form(instance=odontogram)
    elif nb_tooth == 't_71':
        tooth_form = forms.T71Form(instance=odontogram)
    elif nb_tooth == 't_72':
        tooth_form = forms.T72Form(instance=odontogram)
    elif nb_tooth == 't_73':
        tooth_form = forms.T73Form(instance=odontogram)
    elif nb_tooth == 't_74':
        tooth_form = forms.T74Form(instance=odontogram)
    elif nb_tooth == 't_75':
        tooth_form = forms.T75Form(instance=odontogram)
    elif nb_tooth == 't_81':
        tooth_form = forms.T81Form(instance=odontogram)
    elif nb_tooth == 't_82':
        tooth_form = forms.T82Form(instance=odontogram)
    elif nb_tooth == 't_83':
        tooth_form = forms.T83Form(instance=odontogram)
    elif nb_tooth == 't_84':
        tooth_form = forms.T84Form(instance=odontogram)
    else:
        tooth_form = forms.T85Form(instance=odontogram)
    if request.method == 'POST':
        # Selection of field
        if nb_tooth == 't_11':
            tooth_form = forms.T11Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_12':
            tooth_form = forms.T12Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_13':
            tooth_form = forms.T13Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_14':
            tooth_form = forms.T14Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_15':
            tooth_form = forms.T15Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_16':
            tooth_form = forms.T16Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_17':
            tooth_form = forms.T17Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_18':
            tooth_form = forms.T18Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_21':
            tooth_form = forms.T21Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_22':
            tooth_form = forms.T22Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_23':
            tooth_form = forms.T23Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_24':
            tooth_form = forms.T24Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_25':
            tooth_form = forms.T25Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_26':
            tooth_form = forms.T26Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_27':
            tooth_form = forms.T27Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_28':
            tooth_form = forms.T28Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_31':
            tooth_form = forms.T31Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_32':
            tooth_form = forms.T32Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_33':
            tooth_form = forms.T33Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_34':
            tooth_form = forms.T34Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_35':
            tooth_form = forms.T35Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_36':
            tooth_form = forms.T36Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_37':
            tooth_form = forms.T37Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_38':
            tooth_form = forms.T38Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_41':
            tooth_form = forms.T41Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_42':
            tooth_form = forms.T42Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_43':
            tooth_form = forms.T43Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_44':
            tooth_form = forms.T44Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_45':
            tooth_form = forms.T45Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_46':
            tooth_form = forms.T46Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_47':
            tooth_form = forms.T47Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_48':
            tooth_form = forms.T48Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_51':
            tooth_form = forms.T51Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_52':
            tooth_form = forms.T52Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_53':
            tooth_form = forms.T53Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_54':
            tooth_form = forms.T54Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_55':
            tooth_form = forms.T55Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_61':
            tooth_form = forms.T61Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_62':
            tooth_form = forms.T62Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_63':
            tooth_form = forms.T63Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_64':
            tooth_form = forms.T64Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_65':
            tooth_form = forms.T65Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_71':
            tooth_form = forms.T71Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_72':
            tooth_form = forms.T72Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_73':
            tooth_form = forms.T73Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_74':
            tooth_form = forms.T74Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_75':
            tooth_form = forms.T75Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_81':
            tooth_form = forms.T81Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_82':
            tooth_form = forms.T82Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_83':
            tooth_form = forms.T83Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_84':
            tooth_form = forms.T84Form(
                request.POST, instance=odontogram)
        else:
            tooth_form = forms.T85Form(
                request.POST, instance=odontogram)
        if tooth_form.is_valid():
            # append to profile
            tooth_form.save()
            messages.success(request,'Estado del diente actualizado!')
            return redirect('record:odontogram_in_codes', pk_mouth=pk_mouth)
    return render(request, 'tooth.html', {
        'tooth_form': tooth_form,
        'pk_mouth': pk_mouth,
        'nb_tooth': nb_tooth,
        }
    )


def update_odonto(request, pk_mouth):
    odontogram = Mouth.objects.get(pk=pk_mouth)
    if request.method == 'POST':
        return redirect('record:tooth', pk_mouth=pk_mouth)
    return render(request, 'odontogram.html', {
        'odontogram': odontogram,
        'pk_mouth': pk_mouth,
        }
    )


def view_odonto(request, pk_mouth):
    odontogram = Mouth.objects.get(pk=pk_mouth)
    treatments = [
        'c1', 'c2', 'c3', 'c4', 'c5',
        'r1', 'r2', 'r3', 'r4', 'r5',
        'e', 'p', 'z', 'd', 'g', 'sano',
    ]
    if request.method == 'POST':
        return redirect('record:tooth', pk_mouth=pk_mouth)
    return render(request, 'odontogram_codes.html', {
        'odontogram': odontogram,
        'pk_mouth': pk_mouth,
        'treatments': treatments,
        }
    )
