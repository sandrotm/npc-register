from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length = 95)
    

class District(models.Model):
    name = models.CharField(max_length = 95)
    region = models.ForeignKey(Region)
    
    
'''class Phone(models.Model):
    value = models.CharField(max_length = 15) 
    type = models.CharField(
        choices = (
            ('mobile', 'მობილური'), 
            ('home', 'სახლის'), 
            ('work', 'სამსახურის')
        ),
        max_length = 12,
    )
    person = models.ForeignKey('Member')'''


class Member(models.Model):
    # identity
    first_name = models.CharField(max_length = 95, verbose_name = 'სახელი')
    last_name = models.CharField(max_length = 95, verbose_name = 'გვარი')
    personal_id = models.CharField(max_length = 12, verbose_name = 'პირადი ნომერი')    
    # contact
    fb_id = models.CharField(max_length = 190, blank = True, null = True)
    email = models.EmailField(verbose_name = 'ელ-ფოსტა', blank = True, null = True)
    phone_type = models.CharField(
        choices = (
            ('mobile', 'მობილური'), 
            ('home', 'სახლის'), 
            ('work', 'სამსახურის')
        ),
        max_length = 12,
    )
    phone = models.CharField(max_length = 15)   
    # location
    district = models.CharField(max_length = 95, verbose_name = 'რაიონი / რეგიონი')    
    settlement = models.CharField(max_length = 95, verbose_name = 'ქალაქი ან სოფელი')
    address = models.CharField(max_length = 190, verbose_name = 'მისამართი')        
    # demographics    
    birth_date = models.DateField(verbose_name = 'დაბადების თარიღი')
    workplace = models.CharField(max_length = 190, verbose_name = 'სამუშაო ადგილი',
        blank = True, null = True)
    position = models.CharField(max_length = 190, verbose_name = 'თანამდებობა', 
        blank = True, null = True)
    '''sex = models.CharField(choices = (('male', 'მამრობითი'), ('female', 'მდედრობითი')),
        max_length = 15) # should we limit to these 2?'''
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
 

    
    
    