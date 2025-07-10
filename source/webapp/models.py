from django.db import models

STATUS_CHOICES = [('new','новая'),('deleted','удаленная'),('old','старое')]

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=False, blank=False)
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50, verbose_name='Автор', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=10,verbose_name='Статус',choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0])


    def __str__(self):
        return f"{self.id} - {self.title}"


    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
