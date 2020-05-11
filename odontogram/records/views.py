from django.contrib import messages
from django.shortcuts import render, redirect


from .forms import ToothForm

def tooth_view(request):
    tooth_form = ToothForm()
    if request.method == 'POST':
        tooth_form = ToothForm(request.POST)
        if tooth_form.is_valid():
            tooth_form.save()
            messages.success(request,'Estado del diente actualizado!')
            return redirect('index')
    return render(request, 'tooth.html', {'tooth_form': tooth_form})


def new_odontogram(request):
    # Create instance
    # Get object
    # set teeth's state
    return render(request, 'odontogram.html')
