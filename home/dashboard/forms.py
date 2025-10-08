from django import forms
from .models import Product, Order, Reservation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['hotel', 'check_in', 'check_out', 'guests', 'special_requests']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hotel'].widget.attrs.update({'class': 'form-control'})
        self.fields['guests'].widget.attrs.update({'class': 'form-control', 'min': 1})

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out and check_out <= check_in:
            self.add_error('check_out', 'La fecha de salida debe ser posterior a la de entrada.')

        return cleaned_data


class HotelFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Buscar',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del hotel', 'class': 'form-control'}),
    )
    city = forms.CharField(
        required=False,
        label='Ciudad',
        widget=forms.TextInput(attrs={'placeholder': 'Ciudad o país', 'class': 'form-control'}),
    )
