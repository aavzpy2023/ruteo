from django.db import models

# Create your models here.
class Farmacias(models.Model):
    """Tabla farmacias"""
    nombre = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)

class Distancias(models.Model):
    """Tabla Distancias

    Args:
        models (_type_): Django object
    """
    origen = models.ForeignKey(Farmacias, on_delete=models.CASCADE, name='origen')
    # destino = models.ForeignKey(Farmacias, on_delete=models.CASCADE, name='destino')
    distancia = models.FloatField()
