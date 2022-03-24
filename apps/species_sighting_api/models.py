from django.db import models

class Place(models.Model):
    name_place = models.CharField(max_length=100)
    country    = models.CharField(max_length=100)
    state      = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'places'

    def __str__(self):
        return f'{self.name_place}'

class TaxonomicCategory(models.Model):
    kingdom = models.CharField(max_length=100)
    phylum  = models.CharField(max_length=100)
    t_class = models.CharField(max_length=100)
    t_order = models.CharField(max_length=100)
    family  = models.CharField(max_length=100)
    genus   = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'taxonomic_ategories'
    
    def __str__(self):
        return f'{self.pk}'

class Specie(models.Model):
    common_name           = models.CharField(max_length=100, unique=True)
    scientific_name       = models.CharField(max_length=100, unique=True)
    pk_taxonomic_category = models.OneToOneField(TaxonomicCategory, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        verbose_name_plural = 'species'
    
    def __str__(self):
        return f'{self.common_name}'

class Sighting(models.Model):
    latitude      = models.FloatField(default=0.0)
    longitude     = models.FloatField(default=0.0)
    author        = models.CharField(max_length=100)
    notes         = models.TextField()
    sighting_date = models.DateTimeField(auto_now_add=True)
    pk_place      = models.OneToOneField(Place, on_delete=models.CASCADE)
    pk_specie     = models.ForeignKey(Specie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'sightings'
    
    def __str__(self):
        return f'{self.author} - {self.pk_place}'
