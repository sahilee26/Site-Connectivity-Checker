from django.db import models
from datetime import datetime


class query(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    urlq = models.CharField(max_length=200)
    messageq=models.CharField(max_length=200)
    statusq = models.IntegerField(default=200)
    timeq=models.DateTimeField(auto_now_add=True)

    class Meta:
    	    indexes = [
	        models.Index(fields=['-timeq'])
	    ]
    def __str__(self):
        return str(self.urlq)

class uquery(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    urlq = models.CharField(max_length=200)
    startq = models.CharField(max_length=200)
    timeq=models.DateTimeField(default=datetime.now)

    class Meta:
    	    indexes = [
	        models.Index(fields=['-timeq'])
	    ]
    def __str__(self):
        return str(self.urlq)
