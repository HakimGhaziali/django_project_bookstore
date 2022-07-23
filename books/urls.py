from django.urls import path
from .views import BookCreate, BookDetailView, BookListView , BookUpdate

urlpatterns = [

   path('', BookListView.as_view() , name='book_list'),
   path('<int:pk>/', BookDetailView.as_view() , name='book_detail'),
   path('new/', BookCreate.as_view() , name='book_create'),
   path('<int:pk>/edit/', BookUpdate.as_view() , name='book_update'),
]
