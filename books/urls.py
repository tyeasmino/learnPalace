from django.urls import path
from . import views
from core.urls import home
urlpatterns = [ 
    path('addBookCategory/', views.addBookCategoryView.as_view(), name='addBookCategory'), 
    path('addBookDetails/', views.addBookDetailsView.as_view(), name='addBookDetails'), 
    path('bookDetails/<int:id>/', views.bookDetailsView.as_view(), name='bookDetails'), 
    path('borrowBook/<int:id>/', views.borrowBookView.as_view(), name='borrowBook'), 
    path('returnBook/<int:id>/', views.returnBookView.as_view(), name='returnBook'), 
    path('report', views.borrowReportView.as_view(), name='borrowreport'), 

    path('category/<slug:category_slug>/', home, name='category_wise_books'),  


    # path('edit/<int:id>/', views.updateInvestigationUpdateView.as_view(), name='edit_investigations'),  
    # path('delete/<int:id>/', views.deleteInvestigationDeleteView.as_view(), name='delete_investigations'), 
]