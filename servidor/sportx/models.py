from django.db import models
from django.forms import ValidationError


class PQRS(models.Model):
    """ Modelo para la tabla de Peticiones Queja Reclamo y Sugerencia """

    """para ordenar las peticiones segun el estado"""
    class OpenPqrs(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='abierto')


    class ClosedPqrs(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='cerrado')

    
    """Opciones de los campos 'identification_type' y 'status' """
    identification_options = (
        ('cedula', 'Cédula'),
        ('tarjeta de identidad', 'Tarjeta de identidad'),
        ('cedula de Extranjería', 'Cedula de Extranjería'),
    )


    status_options = ( 
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    )
    


    """ Campos de la tabla """
    identification = models.IntegerField()
    identification_type = models.CharField(
        max_length=25, 
        choices=identification_options, 
        default='cedula', 
        verbose_name='Tipo de identificación', 
        help_text='Tipo de identificación', 
        blank=False, null=False
    )
    name = models.CharField(max_length=100, verbose_name='Nombre', help_text='Nombre', blank=False, null=False)
    last_name = models.CharField(max_length=100, verbose_name='Apellido', help_text='Apellido', blank=False, null=False)
    movil = models.IntegerField( blank=True, null=True, verbose_name='Móvil', help_text='Móvil')
    phone = models.IntegerField(blank=True, null=True, verbose_name='Teléfono', help_text='Teléfono')
    email = models.EmailField(max_length=100, verbose_name='Email', help_text='Email', blank=False, null=False)
    title = models.CharField(max_length=100, verbose_name='Título', help_text='Título', blank=False, null=False)
    description = models.TextField(verbose_name='Descripción', help_text='Descripción', blank=False, null=False)
    status = models.CharField(max_length=10, choices=status_options, default='abierto')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    openpqrs = OpenPqrs()
    closedpqrs = ClosedPqrs()


    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'
        ordering = ['created_at']


    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)