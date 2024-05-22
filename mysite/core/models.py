from django.db import models

# Create your models here.

class Nodes(models.Model):
    """Tabla Nodes
    
    Args:
        models (_type_): Django object
    """
    name = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    distr_center = models.CharField(max_length=50, name='CD')
    
    class Meta:
        verbose_name_plural = 'Nodes'
    

class StreetSections(models.Model):
    """Tabla Sections

    Args:
        models (_type_): Django object
    """
    origin = models.ForeignKey(Nodes, on_delete=models.CASCADE, name='origin')
    destiny = models.CharField(max_length=50)
    distance = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'Sections'

class Routes(models.Model):
    """Tabla Routes

    Args:
        models (_type_): Django object
    """
    
    calculation_date = models.DateField()
    node_id_ci = models.ForeignKey(Nodes, on_delete=models.CASCADE, 
                                   name='distributor center')
    nodes_list = models.CharField(max_length=1000)
    opt_route = models.CharField(max_length=1000)
    tot_distance = models.FloatField(name='distance')
    
    class Meta:
        verbose_name_plural = 'Routes'

# class Roles(models.Model):
#     """Table Roles

#     Args:
#         models (_type_): Django object
#     """
#     name = models.CharField(max_length=500)
#     permissions = models.CharField(max_length=500)
    
#     class Meta:
#         verbose_name_plural = 'Roles'