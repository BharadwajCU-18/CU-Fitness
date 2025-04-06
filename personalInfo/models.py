from django.db import models

from django.contrib.auth.models import User  # Assuming you are using Django's default User model

class FitnessInformation(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dietary_preferences = models.CharField(max_length=100, null=True, blank=True)
    fitness_goals = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Fitness Info: {self.age} years old"



class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"

