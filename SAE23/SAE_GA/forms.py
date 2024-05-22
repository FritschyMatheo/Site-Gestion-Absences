from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class GroupeForm(ModelForm):
        class Meta:
            model = models.Groupe
            fields = ('nom',)
            labels = {
            'nom' : _('Nom'),
            }