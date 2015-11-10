from django.db import models


'''class Region(models.Model):
    name = models.CharField(max_length = 95)
    

class District(models.Model):
    name = models.CharField(max_length = 95)
    region = models.ForeignKey(Region)
    
    
class Phone(models.Model):
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
# break down for 3 or more parameters


class Member(models.Model):
    # identity
    first_name = models.CharField(max_length = 95, verbose_name = 'სახელი')
    last_name = models.CharField(max_length = 95, verbose_name = 'გვარი')
    personal_id = models.CharField(
        max_length = 36, 
        unique = True,
        verbose_name = 'პირადი ნომერი',        
    ) 
    email_confirm = models.CharField(max_length = 95, 
        choices = (
            ('fail', 'ვერ გაიგზავნა'),
            ('unconfirmed', 'გაიგზავნა, მაგრამ არ დაუდასტურებია'),
            ('confirmed', 'დაადასტურა'),
        ),
        default = 'fail',
    )
    member_confirm_id = models.CharField(max_length = 12, unique = True, 
        verbose_name = 'წევრის უნიკალური იდენტიფიკატორი', blank = True, null = True)
    # contact
    fb_id = models.CharField(max_length = 190, blank = True, null = True)
    email = models.EmailField(verbose_name = 'ელ-ფოსტა')
    phone_type = models.CharField(
        choices = (
            ('mobile', 'მობილური'), 
            ('home', 'სახლის'), 
            ('work', 'სამსახურის')
        ),
        max_length = 12,
        default = 'mobile',
    )
    phone = models.CharField(max_length = 15, blank = True, null = True)   
    # confirmation
    email_confirm = models.CharField(
        max_length = 95, 
        choices = (
            ('fail', 'ვერ გაიგზავნა'),
            ('unconfirmed', 'გაიგზავნა, მაგრამ არ დაუდასტურებია'),
            ('confirmed', 'დაადასტურა'),
        ),
        default = 'fail',
    )
    member_confirm_id = models.CharField(
        max_length = 40, 
        unique = True,
        blank = True, null = True,
        verbose_name = 'წევრის უნიკალური იდენტიფიკატორი',
    )    
    # location
    district = models.CharField(max_length = 95, verbose_name = 'რაიონი / რეგიონი')    
    settlement = models.CharField(max_length = 95, verbose_name = 'ქალაქი ან სოფელი')
    address = models.CharField(max_length = 190, verbose_name = 'მისამართი')        
    # demographics    
    birth_date = models.DateField(verbose_name = 'დაბადების თარიღი')
    workplace = models.CharField(
        max_length = 190, 
        blank = True, null = True,
        verbose_name = 'სამუშაო ადგილი',)       
    sex = models.CharField(max_length = 15, 
        choices = (
            ('unknown', 'უცნობი'),
            ('male', 'მამრობითი'), 
            ('female', 'მდედრობითი'),
            ('other', 'სხვა'),
        ),
        default = 'unknown',
        blank = True, 
        null = True,
    )
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name = 'წევრი'    
 

    
    
    
