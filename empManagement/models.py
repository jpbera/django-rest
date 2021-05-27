from django.db import models

from RestApi.storage_backends import PublicMediaStorage, StaticStorage,PrivateMediaStorage
# Create your models here.
class Company(models.Model):
    c_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='C_ID')
    c_name = models.CharField(max_length=50)
    c_address = models.CharField(max_length=1000)

    def __str__(self) :
        return (self.c_name)
    class Meta:
        db_table = "Company"
        verbose_name = 'Company'


class Employee(models.Model):
    e_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='e_ID')
    e_name = models.CharField(max_length=50)
    e_phone = models.BigIntegerField()
    e_address = models.CharField(max_length=1000)
    e_pic=models.ImageField(storage=StaticStorage())
    e_email=models.EmailField(max_length=254)
    c_name=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company')

    def __str__(self):
     return '%s: %s' % (self.c_name, self.e_name)
    class Meta:
     db_table = "Employee"
     verbose_name = 'Employee'

class Client(models.Model):
    client_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Client_ID')
    client_name = models.CharField(max_length=500)

    def __str__(self) :
        return (self.client_name)
    class Meta:
        db_table = "Client"
        verbose_name = 'Client'

        

 



""" class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PublicMediaStorage())


class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage()) """

""" from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) """

"""   s3=boto3.resource('s3', region_name='us-east-2' ,
aws_access_key_id='AKIAZRFPUD7EWIH2COUZ',
aws_secret_access_key= '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'
)        
# response = s3.list_buckets()
# Print out bucket names
for bucket in s3.buckets.all():
print(bucket.name) """