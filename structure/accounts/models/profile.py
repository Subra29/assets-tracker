'''
This file created for Profile setup 
'''

from django.db import models

from mainConfig.models.mixin import TimeStampMixin


## Profile Class 

class Profile(TimeStampMixin):
    user = models.OneToOneField(
        "accounts.User",on_delete= models.CASCADE,null=True,
        related_name='profile'
    )
    full_name = models.CharField(
        max_length=400,null=True
    )
    phone = models.CharField(
        max_length=11,null=True,unique=True
    )

    def __str__(self):
        return str(self.full_name)

    class Meta:
        verbose_name_plural = "Profile"
        indexes = [models.Index(fields=['id','user','phone'])]

