from django.shortcuts import render

from .forms import MouthForm

def new_odontogram(request):
    mouth_form = MouthForm()
    return render(request, 'odontogram.html', {
        'mouth_form': mouth_form,}
    )
