from rest_framework import generics
from books.models import Book

from .serializer import BookSerializer


# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all() # configuracion de la consulta, todos los objetos
    serializer_class = BookSerializer # asocio el modelo con el serializador
    