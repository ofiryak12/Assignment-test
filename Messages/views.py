from .models import Data_msg
from .serializers import DataSerializer_readall, DataSerializer_write
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

class Read_Msgs(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = Data_msg.objects.filter(reciever=request.user)
        serializer = DataSerializer_readall(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DataSerializer_write(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class Read_unread_Msgs(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data = Data_msg.objects.filter(read=False,reciever=request.user)
        serializer = DataSerializer_readall(data,many=True)
        return Response(serializer.data)


class SingleMessageView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Data_msg.objects.all()
    serializer_class = DataSerializer_readall

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        data.read = True
        data.save()
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def delete(self,request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



