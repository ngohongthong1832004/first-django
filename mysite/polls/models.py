from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    




class TestImport(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.text
    
class ListStudent(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=200, default='SOME STRING')
    last_name = models.CharField(max_length=200, default='SOME STRING')
    age = models.IntegerField(default=0)
    def __str__(self): 
        return self.first_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
