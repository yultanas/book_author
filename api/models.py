from tastypie.resources import ModelResource
from book.models import Book, Author
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'authors'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        allowed_methods = ['get', 'post', 'delete']
        # можно исллючить
        # excludes = ['book_id']
        authentication = CustomAuthentication()
        authorization = Authorization()
    # влияет на то, как обрабатываются данные,
    # которые приходят от клиента и идут на сервер

    def hydrate(self, bundle):
        bundle.obj.author_id = bundle.data['author_id']
        return bundle
    # влияет на то, как данные возвращаются клиенту

    def dehydrate(self, bundle):
        bundle.data['author_id'] = bundle.obj.author_id
        bundle.data['author'] = bundle.obj.author
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
