from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


#Place
class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Place(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    users = models.ManyToManyField(UserProfile)

    def __str__(self) -> str:
        return f"{self.users}--{self.city}-{self.district}-{self.region}-{self.country}"
