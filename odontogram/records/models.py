from django.db import models
from django.utils.timezone import now


class Mouth(models.Model):
    """
    Odontogram, the fact that teeth were distributed
    inside a mouth model, and not as single instances
    in a model 'tooth' was to avoid excesive database
    hits when displaying the main odontogram in patient
    general information
    """
    date = models.DateTimeField(default=now, editable=False)
    t_11 = models.CharField(max_length=90, default='sano')
    t_12 = models.CharField(max_length=90, default='sano')
    t_13 = models.CharField(max_length=90, default='sano')
    t_14 = models.CharField(max_length=90, default='sano')
    t_15 = models.CharField(max_length=90, default='sano')
    t_16 = models.CharField(max_length=90, default='sano')
    t_17 = models.CharField(max_length=90, default='sano')
    t_18 = models.CharField(max_length=90, default='sano')
    t_21 = models.CharField(max_length=90, default='sano')
    t_22 = models.CharField(max_length=90, default='sano')
    t_23 = models.CharField(max_length=90, default='sano')
    t_24 = models.CharField(max_length=90, default='sano')
    t_25 = models.CharField(max_length=90, default='sano')
    t_26 = models.CharField(max_length=90, default='sano')
    t_27 = models.CharField(max_length=90, default='sano')
    t_28 = models.CharField(max_length=90, default='sano')
    t_31 = models.CharField(max_length=90, default='sano')
    t_32 = models.CharField(max_length=90, default='sano')
    t_33 = models.CharField(max_length=90, default='sano')
    t_34 = models.CharField(max_length=90, default='sano')
    t_35 = models.CharField(max_length=90, default='sano')
    t_36 = models.CharField(max_length=90, default='sano')
    t_37 = models.CharField(max_length=90, default='sano')
    t_38 = models.CharField(max_length=90, default='sano')
    t_41 = models.CharField(max_length=90, default='sano')
    t_42 = models.CharField(max_length=90, default='sano')
    t_43 = models.CharField(max_length=90, default='sano')
    t_44 = models.CharField(max_length=90, default='sano')
    t_45 = models.CharField(max_length=90, default='sano')
    t_46 = models.CharField(max_length=90, default='sano')
    t_47 = models.CharField(max_length=90, default='sano')
    t_48 = models.CharField(max_length=90, default='sano')
    t_51 = models.CharField(max_length=90, default='sano')
    t_52 = models.CharField(max_length=90, default='sano')
    t_53 = models.CharField(max_length=90, default='sano')
    t_54 = models.CharField(max_length=90, default='sano')
    t_55 = models.CharField(max_length=90, default='sano')
    t_61 = models.CharField(max_length=90, default='sano')
    t_62 = models.CharField(max_length=90, default='sano')
    t_63 = models.CharField(max_length=90, default='sano')
    t_64 = models.CharField(max_length=90, default='sano')
    t_65 = models.CharField(max_length=90, default='sano')
    t_71 = models.CharField(max_length=90, default='sano')
    t_72 = models.CharField(max_length=90, default='sano')
    t_73 = models.CharField(max_length=90, default='sano')
    t_74 = models.CharField(max_length=90, default='sano')
    t_75 = models.CharField(max_length=90, default='sano')
    t_81 = models.CharField(max_length=90, default='sano')
    t_82 = models.CharField(max_length=90, default='sano')
    t_83 = models.CharField(max_length=90, default='sano')
    t_84 = models.CharField(max_length=90, default='sano')
    t_85 = models.CharField(max_length=90, default='sano')
