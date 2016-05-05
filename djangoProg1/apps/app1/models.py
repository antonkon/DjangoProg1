from django.db import models

# Create your models here.
class Interview(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Dirst name")
    second_name = models.CharField(max_length=30, verbose_name="Second name")
    email = models.EmailField(max_length=30, verbose_name="Email")
    text = models.CharField(verbose_name="Text interview :")
    date = models.DateField(auto_now_add=True, verbose_name="Data")

    def __str__(self):
        return u'{0}'.format(self.first_name)

    class Meta:
        verbose_name = "interview"
        verbose_name_plural = "interviews"