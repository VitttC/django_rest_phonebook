from django.db import models

"""
Contact model to store contacts.
If a country code is not provided it is supposed to be Italian and +39 will be used.
"""
class Contact(models.Model):
    owner = models.ForeignKey('auth.user', related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, default='')
    country_code = models.CharField(max_length=5, default='+39')
    phone_number = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']