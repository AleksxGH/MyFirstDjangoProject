from django.db import models

class Article(models.Model):
    title = models.CharField("Название", max_length=50)
    date = models.DateTimeField("Дата публикации")
    author = models.CharField("Автор", max_length=50)
    resource = models.CharField("Источник", max_length=150)
    content = models.TextField("Статья")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/articles/{self.id}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"