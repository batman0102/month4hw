from django import forms
from clothes.models import Clothes, Review, Tag
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

class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Поиск',
                'class': 'form-control'
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    orderings = (
        ('name', 'По заголовку'),
        ('-name', 'По заголовку (обратно)'),
        ('created_at', 'По дате создания'),
        ('-created_at', 'По дате создания (обратно)')
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )