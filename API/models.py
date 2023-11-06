from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create a model for the course
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create a model for student
class Student(models.Model):
    GROUP_CHOICES = (
        ('A', 'Group A'),
        ('B', 'Group B'),
        ('C', 'Group C'),
    )
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)
    question_1 = models.BooleanField(default=False)
    question_2 = models.BooleanField(default=False)
    question_3 = models.BooleanField(default=False)
    question_4 = models.BooleanField(default=False)
    question_5 = models.BooleanField(default=False)
    question_6 = models.BooleanField(default=False)
    question_7 = models.BooleanField(default=False)
    question_8 = models.BooleanField(default=False)
    question_9 = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    courses_enrolled = models.ManyToManyField('Course', related_name='students')
    # Add punctuations
    punctuation = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Calculate the count of true boolean values
        true_questions = [self.question_1, self.question_2, self.question_3, self.question_4, self.question_5, self.question_6, self.question_7, self.question_8, self.question_9]
        self.punctuation = sum(true_questions)
        super(Student, self).save(*args, **kwargs)
