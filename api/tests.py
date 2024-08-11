from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from book.models import Author, Book
from api.models import AuthorResource, BookResource


class AuthorResourceTest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.author = Author.objects.create(name="Author Name")
        self.author_resource = AuthorResource()

    def _auth_headers(self):
        return {'Authorization': 'ApiKey adminbook:tanas12345'}

    def test_get_author(self):
        response = self.api_client.get(
            '/api/v1/authors/', format='json', **self._auth_headers())
        self.assertValidJSONResponse(response)
        self.assertEqual(len(self.deserialize(response)['objects']), 1)


class BookResourceTest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(title="Book Title", author=self.author)
        self.book_resource = BookResource()

    def _auth_headers(self):
        return {'Authorization': 'ApiKey adminbook:tanas12345'}

    def test_get_book(self):
        response = self.api_client.get(
            '/api/v1/books/', format='json', **self._auth_headers())
        self.assertValidJSONResponse(response)
        self.assertEqual(len(self.deserialize(response)['objects']), 1)
