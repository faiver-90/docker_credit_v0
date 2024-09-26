from django import forms

from apps.questionnaire.models import *


class MyForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput(attrs={'class': 'form-control', 'multiple': True})

    def to_python(self, data):
        if not data:
            return []
        if not isinstance(data, list):
            return [data]
        return data


class ClientUploadDocumentForm(forms.ModelForm):
    document_files = MultipleFileField(required=True)

    def __init__(self, *args, **kwargs):
        super(ClientUploadDocumentForm, self).__init__(*args, **kwargs)

        self.fields['document_type'].required = False
        self.fields['document_files'].required = False
        self.fields['document_files'].label = 'Документ'

    class Meta:
        model = ClientDocument
        fields = ['document_type', 'document_files']  # Добавляем поле document_files
        widgets = {
            'document_type': forms.Select(attrs={'class': 'form-select'}),
        }
