from django.db import models
from django.utils.text import slugify

# Create your models here.

class Skills(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} from {self.company}"

class Location(models.Model):
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city}, {self.state}"

class JobPost(models.Model):
    JOB_TYPE_CHOICES =[
        ('Full Time','Full Time'),
        ('Part Time', 'Part time'),
    ]
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    salary=models.IntegerField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    slug=models.SlugField(null=True,max_length=40,unique=True)
    author= models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    skills= models.ManyToManyField(Skills)
    job_type= models.CharField(max_length=200,null=False,choices=JOB_TYPE_CHOICES)
    

    def save(self, *args, **kwargs):
        if not self.id:  # type: ignore
            self.slug= slugify(self.title)
        return super(JobPost,self).save(*args,**kwargs)            

    def __str__(self):
        return self.title


NEWSLETTER_OPTION = [
    ('W','Weekly'),
    ('M','Monthly')
]

# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default='M')