from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from .models import SecurityQuestion , Register
from .serializers import SecurityQuestionSerializer , PasswordHistorySerializer ,DeviceSerializer 
import random
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['POST'])
def register(request):
    try:
        user = Register.objects.get(email=request.data['email'])
    except:
        return JsonResponse({"msg":"please contact your administrator","result":"0","data":''})
    if user is not None:
        sample_string = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXVCBNM1234567890!@#$%?&*"
        pin = ''.join((random.choice(sample_string))for x in range(8))
        user.pin = pin
        user.companyName = request.data['companyName']
        user.phone = request.data['phone']
        user.save()
        userdetails ={"userId":user.id,"token":""} 

        refresh = RefreshToken.for_user(user)
      
        data = {"userinfo": userdetails}
        content = {"msg":"User register successfully!!","result":"1","data":data,'refresh': str(refresh),'access': str(refresh.access_token)} 
        return JsonResponse(content,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def SecurityQuestionsAll(request):
    questions = SecurityQuestion.objects.all()
    serializer = SecurityQuestionSerializer(questions,many=True)
    content = {"msg":"Security Question successfully!!","result":"1","data":serializer.data}
    return JsonResponse(content,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def verifyPin(request):
    try:
        user = Register.objects.get(id=request.data['userId'],pin=request.data['pin'])
    except:
        return JsonResponse({"msg":"Sorry.Password not matched",'result':'0','data':''})
    if user is not None:
        user.securityQuestion = request.data['securityQuestion']
        user.securityAnswer = request.data['securityAnswer']
        user.save()
        content = {"msg":"pin match successfully!!","result":"1","data":''} 
        return JsonResponse(content,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def savePassword(request):    
    if request.data['userId'] is not None:
        user = Register.objects.get(id=request.data['userId'],)
        user.password = request.data['password']
        user.status = '1'
        user.save()

        passwordHistoryserializer = PasswordHistorySerializer(data=request.data)
        if passwordHistoryserializer.is_valid():
            passwordHistoryserializer.userId = request.data['userId']
            passwordHistoryserializer.password = request.data['password']
            passwordHistoryserializer.save()
            content = {"msg":"password save successfully!!","result":"1","data":''} 
            return JsonResponse(content,status=status.HTTP_201_CREATED)
        else:
            content = {"msg":"Password not saved","result":"0","data":''} 
            return JsonResponse(content,status=status.HTTP_201_CREATED)
    else:
        content = {"msg":"password not saved","result":"0","data":''} 
        return JsonResponse(content,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def changePassword(request):    
        try:
            user = Register.objects.get(id=request.data['userId'],password=request.data['oldPassword'])
        except:
            return JsonResponse({"msg":"Sorry.Password not matched!",'result':'0','data':''})
    
        if user is not None:
            user.password = request.data['newPassword']
            user.save()
               
            #passworddetails = PasswordHistory.objects.get(userId=request.data['userId'],password=request.data['newPassword'])
            #if passworddetails is not None: 
             #   passworddetails.password = request.data['newPassword']
              #  passworddetails.save()
               
            content = {"msg":"password changed successfully!","result":"1","data":''} 
            return JsonResponse(content,status=status.HTTP_201_CREATED)
            #else:
            #   return JsonResponse({"msg":"Sorry.Password not matched!",'result':'0','data':''})
        else:
            return JsonResponse({"msg":"Sorry.Password not matched!111",'result':'0','data':''})

@api_view(['POST'])
def forgotPassword(request):    
    try:
        user = Register.objects.get(email=request.data['email'],status='1')
    except:
        return JsonResponse({"msg":"Email not register",'result':'0','data':''})
    if user is not None:
        sample_string = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXVCBNM1234567890!@#$%?&*"
        pin = ''.join((random.choice(sample_string))for x in range(8))
        user.pin = pin
        user.save()
        content = {"msg":"email sent successfully!!","result":"1","data":''} 
        return JsonResponse(content,status=status.HTTP_201_CREATED)
 

@api_view(['POST'])
def resetPassword(request):    
    try:
        user = Register.objects.get(email=request.data['email'],pin=request.data['pin'],securityQuestion=request.data['securityQuestion'],securityAnswer=request.data['securityAnswer'])
    except:
        return JsonResponse({"msg":"Pin not match",'result':'0','data':''})
    if user is not None:
        content = {"msg":"Password save successfully!!","result":"1","data":''} 
        return JsonResponse(content,status=status.HTTP_201_CREATED)
 
@api_view(['POST'])
def addDevice(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        content = {"msg":"Device added successfully!!","result":"1","data":''}
        return JsonResponse(content,status=status.HTTP_201_CREATED)
    else:
        content = {"msg":serializer.errors,"result":"0","data":""}
        return JsonResponse(content,status=status.HTTP_401_UNAUTHORIZED)
