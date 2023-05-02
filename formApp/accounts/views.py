from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from .models import UserProfile


class SignUpView(SuccessMessageMixin, View):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class
        context = {'forms': form}

        return render(request, self.template_name, context=context)

    def post(self, request):
        data = self.request.POST
        print(data)
        try:
            user_detail = User(first_name=data['firstname'], last_name=data['lastname'],
                            username=data['username'], email=data['username'])
            user_detail.set_password(data['password'])
            user_detail.save()
            user_profile = UserProfile(user=user_detail)
            user_profile.mobile_number = data['mobile_number']
            user_profile.save()
        except:
            messages.error(self.request, 'User Already Exists')
        
        return HttpResponseRedirect(request.path_info)
