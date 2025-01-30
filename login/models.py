from django.db import models
# from django.core.exceptions import ValidationError
# import re
# Create your models here.



# def validate_email_domain(value):
#     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|yahoo|mnk)$', value):
#         raise ValidationError("Invalid email domain. Allowed domains: .com, .yahoo, .mnk")

# class auth_user(models.Model):
#     email = models.EmailField(validators=[validate_email_domain])

# def save(self, *args, **kwargs):
#         # Enforce validation
#         self.full_clean()
#         super(auth_user, self).save(*args, **kwargs)