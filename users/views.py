from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from .constants import *

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET, algorithm=HASH_ALGORITHM)

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt', None)
        if not token:
            raise AuthenticationFailed('You are not authenticated!')

        try:
            payload = jwt.decode(token, SECRET, algorithms=[HASH_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('You are not authenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class ViewUsers(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt', None)
        if not token:
            raise AuthenticationFailed('You are not authenticated!')

        try:
            payload = jwt.decode(token, SECRET, algorithms=[HASH_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('You are not authenticated!')

        user = User.objects.filter(id=payload['id']).first()
        if not user.is_staff:
            raise AuthenticationFailed("You are authenticated but not authorized, sign in with a privileged account")
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'You were logged out successfully'
        }
        return response
