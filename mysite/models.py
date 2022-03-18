from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class picture(models.Model):
    image = models.CharField(max_length=200)
    information = models.CharField(max_length=200)
    rank = models.IntegerField()
    class Meta:
        ordering = ["rank"]

class ZipFile(models.Model):
    packeage_name = models.CharField(max_length=100)
    zip_file = models.FileField()
    def __str__(self):
        return str(self.packeage_name)
# Create your models here.
