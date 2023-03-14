from django.db import models

class Place(models.Model):
    '''
        Modelo de la tabla Place representa un 
        lugar en el cual se ha realizado el 
        avistamiento de una especie.
    '''
    name_place = models.CharField(max_length=100)
    country    = models.CharField(max_length=100)
    state      = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'Place'
        verbose_name_plural = 'Places'
        ordering            = ['name_place']

    def __str__(self):
        return f'{self.name_place}'

class Specie(models.Model):
    '''
        Modelo de la tabla Specie representa
        una especie.
    '''
    common_name           = models.CharField(max_length=100, unique=True)
    scientific_name       = models.CharField(max_length=100, unique=True)
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name        = 'Specie'
        verbose_name_plural = 'Species'
        ordering            = ['common_name']
    
    def __str__(self):
        return f'{self.scientific_name}'

class TaxonomicCategory(models.Model):
    '''
        Modelo de la tabla TaxonomicCategory 
        representa la categoria taxonómica a 
        la que pertenece una especie.
    '''
    kingdom    = models.CharField(max_length=150)
    phylum     = models.CharField(max_length=150)
    t_class    = models.CharField(max_length=150)
    t_order    = models.CharField(max_length=150)
    family     = models.CharField(max_length=150)
    genus      = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_specie = models.ForeignKey('Specie', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name        = 'Taxonomic Category'
        verbose_name_plural = 'Taxonomic Categories'
        ordering            = ['kingdom']
    
    def __str__(self):
        return f'{self.kingdom}'

class Sighting(models.Model):
    '''
        Modelo de la tabla Sighting representa
        un avistamiento de una especie.
    '''
    latitude       = models.FloatField(null=False, blank=False)
    longitude      = models.FloatField(null=False, blank=False)
    image_sighting = models.TextField(null=True, blank=True)
    notes          = models.TextField(null=False, blank=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    id_place       = models.ForeignKey(Place, on_delete=models.CASCADE)
    id_specie      = models.ForeignKey(Specie, on_delete=models.CASCADE)
    id_user        = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name        = 'Sighting'
        verbose_name_plural = 'Sightings'
        ordering            = ['id_user']
    
    def __str__(self):
        return f'{self.id_user.username}'
