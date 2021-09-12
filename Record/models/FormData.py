from django.db import models


class RecordFormData(models.Model):
    fireno = models.CharField(max_length = 50)
    ipc = models.CharField(max_length = 50)
    



  