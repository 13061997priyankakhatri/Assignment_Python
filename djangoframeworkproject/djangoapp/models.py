from django.db import models

# Create your models here.
class Framework(models.Model):
    email = models.EmailField(unique = True, max_length = 20)
    password = models.CharField(max_length=8)
    role = models.CharField(max_length=20) #framework / django
    isActive = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + "& " +self.role 
 
class Django(models.Model):
    userid = models.ForeignKey(Framework, on_delete = models.CASCADE)
    fname = models.CharField(max_length = 12)
    lname = models.CharField(max_length = 12)
    contact = models.CharField(max_length = 10)
    houseno = models.CharField(max_length = 4,null = False)
    blockno = models.CharField(max_length = 2)
    pic = models.FileField(upload_to="media/upload",default="profile.png")

    def __str__(self):
        return self.fname + " " + self.lname + " | " + self.contact + " | " + self.houseno + " | " + self.blockno
    
class member(models.Model):
    userid = models.ForeignKey(Framework, on_delete = models.CASCADE)
    fname = models.CharField(max_length = 12)
    lname = models.CharField(max_length = 12)
    contact = models.CharField(max_length = 10)
    houseno = models.CharField(max_length = 4,null = False)
    blockno = models.CharField(max_length = 2)
    occupation = models.CharField(max_length = 20)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length=15)
    vehicle_details = models.CharField(max_length = 5)
    pic = models.FileField(upload_to="media/upload",default="profile.png")
