from django import forms

from .models import Mouth


CHOICES = (
    ('sano', 'sano'),
    ('c1', 'c1'),
    ('c2', 'c2'),
    ('c3', 'c3'),
    ('c4', 'c4'),
    ('c5', 'c5'),
    ('r1', 'r1'),
    ('r2', 'r2'),
    ('r3', 'r3'),
    ('r4', 'r4'),
    ('r5', 'r5'),
    ('e', 'e'),
    ('p', 'p'),
    ('z', 'z'),
    ('d', 'd'),
    ('a', 'a'),
)

class ToothForm(forms.ModelForm):
    t_11 = forms.MultipleChoiceField(
        choices=CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_11', ]
