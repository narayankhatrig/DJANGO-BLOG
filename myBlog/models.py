from django.db import models

# Create your models here.

class Post(models.Model):
    blog_title = models.CharField(max_length=500)
    blog_post = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    time_published = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.blog_title


    

    
    
