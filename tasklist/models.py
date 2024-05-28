from django.db import models


# Create your models here.
class Manager(models.Model):
    title = models.CharField('Name of the homework', max_length=500)
    is_complete = models.BooleanField('Finished homework', default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

