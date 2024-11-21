from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, ExpenseListCreate, ExpenseRetrieveUpdateDestroy, expenses_by_date_range, category_summary

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroy.as_view(), name='expense-detail'),
    path('expenses/user/<int:user_id>/range/<str:start_date>/<str:end_date>/', expenses_by_date_range, name='expenses-by-date-range'),
    path('expenses/user/<int:user_id>/summary/<int:year>/<int:month>/', category_summary, name='category-summary'),
]
