from django.db import models




# Create your models here.

class Book(models.Model):
    name = models.CharField('nombre del libro', max_length=50, blank=False, null=False, unique=True)
    description = models.TextField('descripcio del libro', blank=False, null=False)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'



    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField('nombre del autor', max_length=1500, blank=False, null=False)
    nationality = models.CharField('nacionalidad', max_length=50, blank=False, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,  verbose_name='Libro')


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


