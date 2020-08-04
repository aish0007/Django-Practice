from django import forms
from .models import Books

class Book_Form(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": 'Your title'}))
    description = forms.CharField(widget=forms.Textarea
        (attrs={
        "class": "new-class-name-two",
        "id": "my-id-for-textarea",
        "rows": 10,
        "cols": 100
    }
    )
    )
    price = forms.DecimalField(initial=199)
    class Meta:
        model = Books
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not title.endswith("edu"):
            return title
        else:
            raise forms.ValidationError("This is not valid")
class RawProductForm(forms.Form):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":'Your title'}))
    description = forms.CharField(widget=forms.Textarea
    (attrs={
        "class":"new-class-name-two",
        "id":"my-id-for-textarea",
        "rows":10,
        "cols":100
    }
    )
    )
    price=forms.DecimalField(initial=199)