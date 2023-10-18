from django.db import models


# Create your models here.




class game_history(models.Model):
    names = (
        ('Randell', 'Randell'),
        ('Mark', 'Mark'),
        ("Tank", "Tank"),
        ('KB', 'KB'),
        ('Gator', 'Gator'),
        ('Soulo', 'Soulo'),
    )
    hometeam = models.CharField(max_length=120, choices=names)
    awayteam = models.CharField(max_length=120, choices=names)
    homescore = models.IntegerField(default=0)
    awayscore = models.IntegerField(default=0)


    def __str__(self):
        return self.hometeam

class standing(models.Model):
    team = models.CharField(max_length=20)
    mp = models.IntegerField(default =0, blank=True)
    percentage = models.FloatField(blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    logo = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.team


