from django.db import models

# Create your models here.
class BoastsRoastsModel(models.Model):
    isroast = models.BooleanField()
    post_content = models.CharField(max_length=280)
    post_upvote = models.IntegerField(default=0)
    post_downvote = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    s_key = models.CharField(max_length=10)
    
    @property 
    def total(self):
        total =   self.post_upvote + self.post_downvote
        return total