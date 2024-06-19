from django.db import models

class PoliticalParty(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100, unique=True)
    



    def __str__(self):
        return self.name

class MP(models.Model):
    name = models.CharField(max_length=100)
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
    
class Sector(models.Model):
    name = models.CharField(max_length=100)
    mp = models.ManyToManyField(MP)

    def __str__(self):
        return f"{self.name} , {self.mp}"

