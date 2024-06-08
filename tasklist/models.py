from django.db import models



# Create your models here.
class Manager(models.Model):
    title = models.CharField('Name of the homework', max_length=500)
    is_complete = models.BooleanField('Finished homework', default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.task.title} by {self.created_at}"


def __str__(self):
    return self.title

