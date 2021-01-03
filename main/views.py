from .models import User,Deal,Message,Start
from .serializers import UserSerializer,DealSerializer,MessageSerializer,StartSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail


'''
    Facade class which contains all 
    what we need to get row
'''
class GetFacadeListOne:
    def __init__(self,modal,serializer):
        self.modal = modal
        self.serializer = serializer

    def get(self,request,num):
        user = self.modal.objects.filter(pk=num)
        ser = self.serializer(user, many=True)
        return Response(data=ser.data)

'''
    Start user api section
'''
class UserLogin(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request):
        user = User.objects.filter(Email=request.data['Email'],Pass=request.data['Pass'])
        USerializer = UserSerializer(user, many=True)
        return Response(data=USerializer.data)

#get one user
class UserOneApi(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(User,UserSerializer)

    def queryset():
        pass

#Get all users 
class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Activate user from url 
class UserActivate(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request,num):
        user = User.objects.get(pk=num)
        user.Activate = 1
        user.save()
        return Response(data=['success'])

class UserRegistr(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            
            message = 'Activate: http://127.0.0.1:8000/api/user/activate/'+str(user.data['id'])
            send_mail('Subject here',message,'poznkirill5@gmail.com',[user.data['Email']],fail_silently=False)
        return Response(status=201)

class UserUpdate(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
    def put(self,request):
        user = UserSerializer(User.objects.get(pk=request.data['id']).id,data=request.data, partial=True)
        if user.is_valid():
            user.save()
        return Response(data=user.save())

'''
    End user api section
'''


'''
    Start deal api section
'''
class DealOneApi(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(Deal,DealSerializer)

    def queryset():
        pass


class DealApi(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class InsertDealApi(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def post(self,request):
        deal = DealSerializer(data=request.data)
        if deal.is_valid():
            deal.save()
        return Response(status=201)


class DeleteDealApi(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def delete(self,request,num):
        deal = Deal.objects.get(pk=num)
        deal.delete()
        return Response(status=201)
'''
    end deal api section
'''



'''
    Start message api section
'''
class MessageApi(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class InsertMessageApi(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self,request):
        Message = MessageSerializer(data=request.data)
        if Message.is_valid():
            Message.save()
        return Response(status=201)
'''
    end message api section
'''


'''
    Start 'start' api section
'''
class StartOneApi(GetFacadeListOne,generics.ListAPIView):
    def __init__(self):
        super().__init__(Start,StartSerializer)

    def queryset():
        pass

class InsertStartApi(generics.ListAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

    def post(self,request):
        Start = StartSerializer(data=request.data)
        if Start.is_valid():
            Start.save()
        return Response(status=201)


class DeleteStartApi(generics.ListAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

    def delete(self,request,num):
        Start = Start.objects.get(pk=num)
        Start.delete()
        return Response(status=201)
'''
    End 'start' api section
'''

