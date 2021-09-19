import threading

from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as log_in, logout as log_out
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, CreateView
import random
from kavenegar import *

from django.core.cache import cache

from .models import SupplierProfile

#phone_cache = caches['phone_verification']


# Create your views here.
from users.models import UserProfile
from utils.email_verification import account_activation_token

from utils.phone_verification import phone_verification


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        if username:
            password = request.POST.get('password', None)
            if password:
                if UserProfile.objects.filter(user__username=username).exists():
                    user = UserProfile.objects.filter(user__username=username)[0]
                    if user.verified:
                        user = authenticate(request, username=username, password=password)
                        if user:
                            log_in(request, user)
                            messages.success(request, 'شما با موفقیت وارد شدید!')
                            return redirect("/")
                        else:
                            messages.error(request, 'نام کاربری یا رمز اشتباه')
                            return redirect("/")
                    else:
                        return HttpResponse("not verified")
        else:
            messages.warning(request, 'نام کاربری الزامی ست')
            return redirect("/")


def logout_view(request):
    log_out(request)
    return redirect('/')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        first_name = request.POST.get("firstname", None)
        last_name = request.POST.get("lastname", None)
        if username:
            if User.objects.filter(username__iexact=username).count() == 0:
                password = request.POST.get('password', None)
                repeated_passweord = request.POST.get('repassword', None)
                if password:
                    if password == repeated_passweord:
                        try:
                            user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name,last_name=last_name,is_active=False)
                            current_site = get_current_site(request)
                            mail_subject = 'Activate your account in GameIN.'
                            message = render_to_string('email_verification.html', {
                                'user': user,
                                'domain': current_site.domain,
                                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                                'token': account_activation_token.make_token(user),
                            })
                            to_email = [request.POST.get('email')]
                            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, to_email)
                            #return HttpResponse('Please confirm your email address to complete the registration')
                            messages.success(request, "Please confirm your email address to complete the registration'")
                            return redirect('/')
                        except IntegrityError as e:
                            # return render(request, "user/error.html", {"message": e})
                            messages.error(request, f"{e}")
                            return redirect('/')
                    else:
                        return HttpResponse("عدم انطباق پسوورد")
            else:
                return HttpResponse("این نام کاربری قبلا ثبت شده است")


def email_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        profile = UserProfile.objects.filter(user_id=uid)[0]
        profile.verified = True
        profile.save()
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def dashboard(request):
    return render(request,'dashboard.html')


def phone_register(request):
    if request.method=='POST':
        code = request.POST.get("code",None)
        print(code)
        print(cache.get(f"code:{request.user.username}"))
        if code:
            if int(cache.get(f"code:{request.user.username}")) == int(code):
                puser = UserProfile.objects.filter(user=request.user.id)[0]
                supplier = SupplierProfile.objects.create(user=puser,rate=3)
                supplier.save()
                return HttpResponse("success")
            else:
                return HttpResponse("code invalid or expired")
        else:
            return HttpResponse("no code")

    if request.method == 'GET':
        return render(request, 'phone_verification.html')


def supplier_register(request):
    if UserProfile.objects.filter(user_id=request.user.id).exists():
        puser = UserProfile.objects.filter(user=request.user.id)[0]
        if puser.phone:
            print(puser.phone)
            thread = threading.Thread(target=phone_verification, args=(puser.user,puser.phone))
            thread.start()
            return redirect('/phone_register/')
        else:
            return HttpResponse("dont have phone")
    else :
        return HttpResponse("!!!")


