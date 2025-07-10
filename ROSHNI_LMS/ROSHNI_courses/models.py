from django.db import models
 
userTypeData = (
    ("Teacher","Teacher"),
    ("Student","Student")
)

class ROSHNI_lmsUser(models.Model):
    userId = models.AutoField(primary_key = True)
    userName = models.CharField(max_length =20)
    email =models.EmailField(unique=True)
    gender =models.CharField(max_length=10,null=True,blank=True)
    number = models.IntegerField(unique=True)
    password = models.CharField(max_length=20)
    userType = models.CharField(max_length=10,choices=userTypeData)

class ROSHNI_courseUpload(models.Model):
    courseUploadId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=20)
    courseDescription = models.CharField(max_length=50)
    createdAt = models.DateField()
    coursePlaylist =models.IntegerField()
    courseDuration = models.CharField(max_length=10)
    userName =models.ForeignKey(ROSHNI_lmsUser,on_delete=models.CASCADE)

