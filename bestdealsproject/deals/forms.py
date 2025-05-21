from django import forms


class ProductSearchForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100)
    min_price = forms.DecimalField(min_value=0.0, max_value=None, required=False, decimal_places=2, max_digits=10)
    max_price = forms.DecimalField(min_value=0.0, max_value=None, required=False, decimal_places=2, max_digits=10)
    category = forms.ChoiceField(choices=[
        ('', 'Any Category'),
        ('furniture', 'Furniture'),
        ('stationery', 'Stationery'),
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        # Add more categories as needed
    ], required=False)
