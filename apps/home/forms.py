from django import forms
from .models import PlayerProfiles, TravelRoutes

class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfiles
        fields = '__all__'


class TravelRouteForm(forms.ModelForm):
    class Meta:
        model = TravelRoutes
        fields = '__all__'