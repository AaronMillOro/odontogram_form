from django.contrib import messages
from django.shortcuts import render, redirect


from .forms import ToothForm

def new_odontogram(request):
    """ Manually modify form """
    tooth_form = ToothForm()
    if request.method == 'POST':
        tooth_form = ToothForm(request.POST)
        # name assigned to the html form for the list
        #selected_values = request.POST.getlist('tooth')
        #print(selected_values)
        if tooth_form.is_valid():
            tooth_form.save()
            messages.success(request,'New oodontogram !')
            return redirect('index')
    return render(request, 'odontogram.html', {'tooth_form': tooth_form})
