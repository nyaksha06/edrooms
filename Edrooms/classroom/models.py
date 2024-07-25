from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.name
    

class Tutorial(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='tutorials/pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Discussion(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Discussion on {self.tutorial.title} by {self.created_by.username}"