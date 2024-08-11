from django.db import models
import uuid


class Author(models.Model):
    author_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, unique=True,
                            blank=False, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(
        max_length=255, unique=True, blank=False, null=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} {self.author}"
