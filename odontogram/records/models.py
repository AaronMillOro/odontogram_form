from django.db import models

TEETH = (
    ('C_11_01', 'C_11_01'),
    ('C_11_02', 'C_11_02'),
    ('C_11_03', 'C_11_03'),
    ('C_11_04', 'C_11_04'),
    ('C_11_05', 'C_11_05'),
)


class Mouth(models.Model):
    """Odontogram"""
    t_11 = models.CharField(max_length=400, choices=TEETH)
