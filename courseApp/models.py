from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return(self.id+self.course_name+self.course_desc+self.rating)
