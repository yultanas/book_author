from django.test import TestCase
from .models import Author, Book
import uuid

# для моделей проверяем создание объектов Author и Book,
# их строковое представление и UUID.


class AuthorModelTest(TestCase):
    def test_create_author(self):
        author = Author.objects.create(name="Author Name")
        self.assertEqual(author.name, "Author Name")
        self.assertIsInstance(author.author_id, uuid.UUID)
        self.assertEqual(str(author), "Author Name")


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author Name")

    def test_create_book(self):
        book = Book.objects.create(title="Book Title", author=self.author)
        self.assertEqual(book.title, "Book Title")
        self.assertEqual(book.author, self.author)
        self.assertIsInstance(book.book_id, uuid.UUID)
        self.assertEqual(str(book), "Book Title Author Name")
