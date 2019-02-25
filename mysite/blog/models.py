from django.db import models

# Create your models here.

class Blog(models.Model):
    """ 博客模型 """
    name = models.CharField(max_length = 100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    """ 作者类型 """
    name = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    """ 博客实体模型类 """
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline