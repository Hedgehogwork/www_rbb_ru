from django.db import models


class CBRF_Deposit(models.Model):
    uploaded_date = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to='cbrf_deposit')
