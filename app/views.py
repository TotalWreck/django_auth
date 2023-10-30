from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

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