from django import forms

from .models import Mouth

TEETH = (
    ('C_11_01', 'C_11_01'),
    ('C_11_02', 'C_11_02'),
    ('C_11_03', 'C_11_03'),
    ('C_11_04', 'C_11_04'),
    ('C_11_05', 'C_11_05'),
)

class MouthForm(forms.Form):
    """ Add a stomatological note """
    t_11 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=TEETH,
    )

    class Meta:
        model = Mouth
        fields = ('t_11', )
