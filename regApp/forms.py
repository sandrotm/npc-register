from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from regApp.models import Member
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
#from django.forms.extras.widgets import TextInput

# Create the form class.
class MemberForm(ModelForm): 
    numeric_only = RegexValidator(r'^[0-9]{11,11}$', 'პირადი ნომერი ზუსტად 11 ციფრისგან შედგება')
    telephone = RegexValidator(r'(\d{3})\D*(\d{3})\D*(\d{3})$')
    YEARS = (x for x in range(1930, 2015))

    personal_id = forms.CharField(validators=[
            numeric_only,
            MinLengthValidator(11),
            MaxLengthValidator(11)
        ], 
        widget = forms.TextInput(attrs = { 
            'size': '11',   
            'required': 'true',
            'placeholder': 'XXXXXXXXXXX',
            'id': 'id_personal_number'
        }),
        max_length = 11,
        min_length = 11,
        label = 'პირადი ნომერი',
    )

    email = forms.EmailField(label='ელ-ფოსტა')

    phone = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder': 'xxx xxx xxx',
        }),
        validators = [telephone], 
        label='ტელეფონის ნომერი',)

    birth_date = forms.DateField(widget = SelectDateWidget(years = YEARS),
        label = 'დაბადების თარიღი')
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'personal_id',
            'email', 'phone_type', 'phone', 'birth_date',)