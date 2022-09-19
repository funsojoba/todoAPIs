from rest_framework import generics,
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIViews):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
     permission_classes = [IsAuthenticated]



class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    
