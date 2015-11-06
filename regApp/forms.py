from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from regApp.models import Member
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
#from django.forms.extras.widgets import TextInput

# Create the form class.
class MemberForm(ModelForm): 
    numeric_only = RegexValidator(r'^[0-9]{11,11}$', 'პირადი ნომერი ზუსტად 11 ციფრისგან შედგება')
    telephone = RegexValidator(r'^([ +()]*\d){0,6}([ ]*\d){5,8}$')
    YEARS = list(reversed(range(1919, 2000))) #[x for x in range(1919, 1999)]
    name_format = RegexValidator(r'^[ ]{0,1}[ა-ჰ]{1,15}[ -]{0,1}[ა-ჰ]{1,15}[ ]{0,1}$')

    first_name = forms.CharField(
        validators=[
            name_format,
            MinLengthValidator(2),
            MaxLengthValidator(20)
        ],                                  
    )
    
    last_name = forms.CharField(
        validators=[
            name_format,
            MinLengthValidator(2),
            MaxLengthValidator(20)
        ],                                  
    )    

    personal_id = forms.CharField(
        validators=[
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

    email = forms.EmailField(label='ელ-ფოსტა')

    phone = forms.CharField(
        validators = [
            telephone,
            MinLengthValidator(7),
            MaxLengthValidator(20)            
        ],                            
        widget = forms.TextInput(attrs = {
            'placeholder': 'XXXXXXXXXXXXXX',
        }),
        max_length = 20,
        min_length = 7,                             
        label='ტელეფონის ნომერი',
    )
    
    birth_date = forms.DateField(
        widget = SelectDateWidget(years = YEARS),
        label = 'დაბადების თარიღი'
    )
    
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'personal_id',
            'email', 'phone_type', 'phone', 
            'district', 'settlement', 'address',
            'birth_date', 'workplace', 'position')
        
