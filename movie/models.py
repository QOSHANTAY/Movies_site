from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name


class Movie(models.Model):
    title = models.CharField(max_length=250,
                                verbose_name='Имя:')
    Year = models.IntegerField(default=2000)
    description = models.TextField()
    poster = models.ImageField(upload_to="images/")
    trailer = models.URLField()
    movie = models.FileField(upload_to='movies/')
    categories = models.ManyToManyField(Category)
    country = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'