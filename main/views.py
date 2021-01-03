from .models import User,Deal,Message,Start
from .serializers import UserSerializer,DealSerializer,MessageSerializer,StartSerializer
from rest_framework import generics, status
from rest_framework.response import Response

class GetFacadeListOne:
    def __init__(self,modal,serializer):
        self.modal = modal
        self.serializer = serializer

    def get(self,request,num):
        user = self.modal.objects.filter(pk=num)
        ser = self.serializer(user, many=True)
        return Response(data=ser.data)




class UserOneListView(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(User,UserSerializer)

    def queryset():
        pass


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InsertListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response(status=201)

    def put(self,request):
        user = UserSerializer(User.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        if user.is_valid():
            user.save()
        return Response(data=user.save())




class DealOneListView(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(Deal,DealSerializer)

    def queryset():
        pass


class DealListView(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class InsertDealListView(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def post(self,request):
        deal = DealSerializer(data=request.data)
        if deal.is_valid():
            deal.save()
        return Response(status=201)


class DeleteDealListView(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def delete(self,request,num):
        deal = Deal.objects.get(pk=num)
        deal.delete()
        return Response(status=201)




class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class InsertMessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self,request):
        Message = MessageSerializer(data=request.data)
        if Message.is_valid():
            Message.save()
        return Response(status=201)




class StartOneListView(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(Start,StartSerializer)

    def queryset():
        pass

class InsertStartListView(generics.ListAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

    def post(self,request):
        Start = StartSerializer(data=request.data)
        if Start.is_valid():
            Start.save()
        return Response(status=201)


class DeleteStartListView(generics.ListAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

    def delete(self,request,num):
        Start = Start.objects.get(pk=num)
        Start.delete()
        return Response(status=201)


