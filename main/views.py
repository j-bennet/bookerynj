from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from .models import Book
from .schemas import BookSchema

api = NinjaAPI()


@api.post("/books")
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}


@api.get("/book/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@api.get("/books", response=list[BookSchema])
def list_books(request):
    qs = Book.objects.all()
    return qs


@api.delete("/books/{book_id}")
def delete_employee(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}
