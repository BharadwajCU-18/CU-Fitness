from django.db import models

from django.contrib.auth.models import User  # Assuming you are using Django's default User model

class FitnessInformation(models.Model):
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    dietary_preferences = models.CharField(max_length=100)
    fitness_goals = models.CharField(max_length=100)

    def __str__(self):
        return f"Fitness Info: {self.age} years old"



class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"

