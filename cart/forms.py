from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', widget=forms.TextInput(attrs={'id': 'quantityInp', 'class': 'quantity_input', 'value':1, 'pattern':'[0-9]' }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
