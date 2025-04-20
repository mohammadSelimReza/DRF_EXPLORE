from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .utilities import generate_otp_code
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.
class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ForgetPassword(APIView):
    def post(self, request):
        email = request.data.get("email")
        existUser = User.objects.get(email=email)
        if existUser:
            otp = generate_otp_code()
            existUser.otp = otp
            # First, render the plain text content.
            text_content = render_to_string(
                "forget_password/index.txt",
                context={"my_variable": 42},
            )
            # Secondly, render the HTML content.
            html_content = render_to_string(
                "forget_password/index.html",
                context={"my_variable": 42, "otp": otp},
            )
            # Then, create a multipart email instance.
            msg = EmailMultiAlternatives(
                "Password Reset Request",
                text_content,
                "srreza1999@gmail.com",
                [email],
                headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
            )
            # Lastly, attach the HTML content to the email instance and send.
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            existUser.save()
            return Response({"message": "User available", "otp": otp})

        else:
            return Response({"message": "User doesn't exist.Try To Create an account."})
