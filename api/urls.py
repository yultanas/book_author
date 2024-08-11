from api.models import AuthorResource, BookResource
from tastypie.api import Api
from django.urls import path, include


# api/v1/authors
# api/v1/books
# для запросов DELETE, POST
# key: Authorization
# value: ApiKey adminbook:tanas12345

api = Api(api_name='v1')


api.register(AuthorResource())
api.register(BookResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
