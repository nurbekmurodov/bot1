from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone']
        labels = {
            'image': _('Rasm'),
            'bio': _('Bio'),
            'phone': _('Telefon raqam'),
        }
