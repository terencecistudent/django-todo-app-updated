from django import forms
from todo.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "done"]
