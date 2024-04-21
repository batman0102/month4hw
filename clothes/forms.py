from django import forms
from clothes.models import Clothes, Review
class ClothForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'image', 'price', 'color', 'size']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название',
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Введите цену',
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'color': forms.TextInput(
                attrs={
                    'placeholder': 'Введите цвет',
                    'class': 'form-control'
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'placeholder': 'Введите размер',
                    'class': 'form-control'
                }
            )
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return price


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Введите отзыв',
                    'class': 'form-control'
                }
            )
        }