from django.db import models
from pytils.translit import slugify


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False,unique=True)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    slug = models.SlugField(max_length=100, verbose_name='Слаг', null=True, blank=True,unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.title}"


    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
