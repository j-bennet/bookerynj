from django.shortcuts import get_object_or_404
from ninja import Query, Router

from .models import Book
from .schemas import BookCreateSchema, BookFilterSchema, BookSchema

router = Router()

@router.post("/books")
def create_book(request, payload: BookCreateSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}


@router.get("/book/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@router.get("/books", response=list[BookSchema])
def list_books(request, filters: BookFilterSchema = Query(...)):
    books = Book.objects.all()
    books = filters.filter(books)
    return books


@router.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}
