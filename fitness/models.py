# from django.db import models
# import datetime

# class FitnessReport(models.Model):
#     date = models.DateField(default=datetime.date.today)
#     steps = models.IntegerField(default=0)
#     cardio_time = models.IntegerField(default=0)  # In minutes
#     cool_down_time = models.IntegerField(default=0)  # In minutes

#     def __str__(self):
#         return f"Progress for {self.date}"
    


# from django.db import models
# from django.contrib.auth.models import User
# import datetime
# from django.core.exceptions import ValidationError

# class FitnessReport(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Associate report with user
#     date = models.DateField(default=datetime.date.today)
#     steps = models.IntegerField(default=0)
#     cardio_time = models.IntegerField(default=0)  # In minutes
#     cool_down_time = models.IntegerField(default=0)  # In minutes

#     def clean(self):
#         if not self.user:
#             raise ValidationError("User field cannot be empty.")
#         if not self.date:
#             raise ValidationError("Date field cannot be empty.")

#     def __str__(self):
#         return f"Progress for {self.user.username} on {self.date}"


from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

class FitnessReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Associate report with user
    date = models.DateField(default=datetime.date.today)
    steps = models.IntegerField(default=0)
    cardio_time = models.IntegerField(default=0)  # In minutes
    cool_down_time = models.IntegerField(default=0)  # In minutes

    def clean(self):
        if not self.user:
            raise ValidationError("User field cannot be empty.")
        if not self.date:
            raise ValidationError("Date field cannot be empty.")

    def __str__(self):
        return f"Progress for {self.user.username} on {self.date}"
