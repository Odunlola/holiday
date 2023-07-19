from django.db import models

class Destination(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    verified_destination = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Spot(models.Model):

    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="spots", default=True)
    verified_spot = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return "Destination" + self.name

    class Meta:
        ordering = ['name']

class List(models.Model):
    name = models.CharField(max_length=150)
    spots = models.ManyToManyField(Spot)

    def __str__(self):
        return self.title