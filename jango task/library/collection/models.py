from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=250)
    Bio = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Name}"


class Publisher(models.Model):
    Name = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Name}"
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    publisher_name = models.CharField(max_length=250)
    publisher_year = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.Title}"



class Post1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"