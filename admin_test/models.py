from django.db import models


class City(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Statistics(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='stats')
    date = models.DateField()
    humidity = models.IntegerField()
    temp_in_c = models.IntegerField()

    def __str__(self):
        return f"{str(self.date)}: {self.city.title}"
