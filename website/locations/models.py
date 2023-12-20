from django.db import models

class Site(models.Model):

    name = models.CharField(max_length = 254)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'locations_sites'
        
class Floor(models.Model):

    site = models.ForeignKey(
        to = Site,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length = 254)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'locations_floors'