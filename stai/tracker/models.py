from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Exercise(models.Model):
    name = 
class Log(models.Model):
    user =
class Workout(models.Model):
    date = 
class Set(models.Model):
    workout = 
    exercise = 
    reps = 
    weight = 
class PlannedWorkout(models.Model):
    date = 
class PlannedSet(models.Model):
    planned_workout = 
    exercise = 
    reps = 
