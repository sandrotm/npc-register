from django import forms
from django.forms import ModelForm
from regApp.models import Member
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
#from django.forms.extras.widgets import TextInput

# Create the form class.
class MemberForm(ModelForm): 
    numeric_only = RegexValidator(r'^[0-9]{11,11}$', 'პირადი ნომერი ზუსტად 11 ციფრისგან შედგება')
    personal_id = forms.CharField(validators=[
            numeric_only,
            MinLengthValidator(11),
            MaxLengthValidator(11)
        ], 
        widget = forms.TextInput(attrs = { 
            'size': '11',   
            'required': 'true',
            'placeholder': 'XXXXXXXXXXX',
        }),
        max_length = 11,
        min_length = 11,
        label = 'პირადი ნომერი',
    )
    
    class Meta:
        model = Member
        fields = '__all__'