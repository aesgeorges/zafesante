from django import forms
from .models import Questions


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('question',)
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Poze yon kesyon',
                    'required': True,
                }
            )
        }
