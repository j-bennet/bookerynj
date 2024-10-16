from ninja import ModelSchema

from .models import Book


class BookSchema(ModelSchema):
    class Meta:
        model = Book
        fields = "__all__"
