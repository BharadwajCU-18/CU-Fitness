
from django import forms
from .models import PaymentInformation

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentInformation
        fields = ['payment_method', 'card_number', 'expiration_date', 'cvv', 'save_for_future']
        widgets = {
            'expiration_date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'cvv': forms.PasswordInput(),
            'card_number': forms.TextInput(attrs={'placeholder': 'XXXX XXXX XXXX XXXX'}),
        }

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if len(card_number) != 16 or not card_number.isdigit():
            raise forms.ValidationError("Enter a valid 16-digit card number.")
        return card_number

    def clean_expiration_date(self):
        exp = self.cleaned_data['expiration_date']
        import re
        if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', exp):
            raise forms.ValidationError("Enter expiration date in MM/YY format.")
        return exp

    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        if len(cvv) not in [3, 4] or not cvv.isdigit():
            raise forms.ValidationError("Invalid CVV.")
        return cvv
