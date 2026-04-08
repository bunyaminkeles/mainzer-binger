from django import forms


class CustomSignupForm(forms.Form):
    sehir = forms.CharField(
        max_length=100,
        required=False,
        label='Şehriniz',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ör: Mainz, Frankfurt, Berlin...',
            'autocomplete': 'address-level2',
        })
    )

    def signup(self, request, user):
        from .models import Profil
        profil, _ = Profil.objects.get_or_create(kullanici=user)
        profil.sehir = self.cleaned_data.get('sehir', '')
        profil.save()
