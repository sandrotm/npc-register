from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from regApp.models import Member
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
#from django.forms.extras.widgets import TextInput

# Create the form class.
class MemberForm(ModelForm): 
    YEARS = list(reversed(range(1919, 2000))) #[x for x in range(1919, 1999)]    
    personal_id_format = RegexValidator(r'^[0-9]{11,11}$', 'პირადი ნომერი ზუსტად 11 ციფრისგან შედგება')
    phone_format = RegexValidator(r'^([ +()]*\d){0,6}([ ]*\d){5,8}$')
    name_format = RegexValidator(r'^[ ]{0,1}[ა-ჰ]{1,20}[ -]{0,1}[ა-ჰ]{1,20}[ ]{0,1}$')
    settlement_format = RegexValidator(r'^[ ]{0,1}[ა-ჰa-zA-Z&]{1,15}[ -]{0,1}[ა-ჰa-zA-Z&]{1,15}[ ]{0,1}$')
    address_format = RegexValidator(r'^[ -/|#,.ა-ჰa-zA-Z&0-9]{5,190}$')
    workplace_format = RegexValidator(r'^[ -/|#,.ა-ჰa-zA-Z&?0-9]{5,190}$')
    position_format = RegexValidator(r'^[ -/|#,.ა-ჰa-zA-Z&0-9]{3,190}$')

    first_name = forms.CharField(
        validators=[
            name_format,
            MinLengthValidator(2),
            MaxLengthValidator(40),
        ], 
        label = 'სახელი',                                 
    )
    
    last_name = forms.CharField(
        validators=[
            name_format,
            MinLengthValidator(2),
            MaxLengthValidator(40)
        ],   
        label = 'გვარი',                               
    )    

    personal_id = forms.CharField(
        validators=[
            personal_id_format,
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
            phone_format,
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
    
    settlement = forms.CharField(
        validators=[
            settlement_format,
            MinLengthValidator(2),
            MaxLengthValidator(40),
        ], 
        label = 'ქალაქი ან სოფელი',            
    )
    
    address = forms.CharField(
        validators=[
            address_format,
            MinLengthValidator(5),
            MaxLengthValidator(190),
        ], 
        label = 'მისამართი',            
    )    
    
    workplace = forms.CharField(
        validators=[
            workplace_format,
            MinLengthValidator(5),
            MaxLengthValidator(190),
        ], 
        label = 'სამუშაო ადგილი',    
    )
    
    position = forms.CharField(
        validators=[
            position_format,
            MinLengthValidator(5),
            MaxLengthValidator(190),
        ], 
        label = 'თანამდებობა',    
    )    
      
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'personal_id',
            'email', 'phone_type', 'phone', 
            'district', 'settlement', 'address',
            'birth_date', 'workplace', 'position')
        
