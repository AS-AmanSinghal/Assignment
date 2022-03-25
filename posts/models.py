from django.db import models
from account.models import MyUser
# Create your models here.


class Posts(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
