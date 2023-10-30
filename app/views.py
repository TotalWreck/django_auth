from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(["GET"])
def index(request):
    return Response("Hello, World!")

@api_view(["POST"])
def register(request):
    User.objects.create_user(
        username = request.data["username"],
        password = request.data["password"])
    return Response({"Authentication":"User created"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def auth(request):
    print(request.user)
    return Response({"Authentication":"Success"})