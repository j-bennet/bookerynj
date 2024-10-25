from ninja import FilterSchema, ModelSchema

from .models import Book


class BookSchema(ModelSchema):
    class Meta:
        model = Book
        fields = "__all__"

class BookCreateSchema(ModelSchema):
    class Meta:
        model = Book
        fields = ["title", "author", "year", "category", "language"]


class BookFilterSchema(FilterSchema):
    language: str | None = None
    category: str | None = None
    author: str | None = None