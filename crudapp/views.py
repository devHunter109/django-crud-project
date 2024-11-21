# from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(['GET'])
def expenses_by_date_range(request, user_id, start_date, end_date):
    expenses = Expense.objects.filter(user_id=user_id, date__range=[start_date, end_date])
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_summary(request, user_id, month, year):
    expenses = Expense.objects.filter(user_id=user_id, date__year=year, date__month=month)
    summary = expenses.values('category').annotate(total=Sum('amount'))
    return Response(summary)


# # Create your views here.
# def orderFormView(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show_url')
#     template_name = 'crudapp/order.html'
#     context = {'form': form}
#     return render(request, template_name, context)

# def showView(request):
#     obj = Orders.objects.all()
#     template_name = 'crudapp/show.html'
#     context = {'obj': obj}
#     return render(request, template_name, context)

# def updateView(request, f_oid):
#     obj = Orders.objects.get(oid=f_oid)
#     form = OrderForm(instance=obj)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect('show_url')
#     template_name = 'crudapp/order.html'
#     context = {'form': form}
#     return render(request, template_name, context)

# def deleteView(request, f_oid):
#     obj = Orders.objects.get(oid=f_oid)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('show_url')
#     template_name = 'crudapp/confirmation.html'
#     context = {'obj': obj}
#     return render(request, template_name, context)
