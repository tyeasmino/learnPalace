from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required 

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string 

def send_transaction_email(user, account_no, mail_subject, template_name):
    message = render_to_string(template_name, {
        'user' : user,
        'account_no' : account_no
    }) 

    send_email = EmailMultiAlternatives(mail_subject, '' ,to=[user.email])
    send_email.attach_alternative(message, "text/html") 
    send_email.send() 


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        

        send_transaction_email(self.request.user, self.request.user.account.account_no, 'Registration Information', 'messages/registration_email.html')
        messages.success(self.request, "Congratulations!! Your registration has been done successfully")
        return super().form_valid(form) 
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        messages.success(self.request, "Login Successful")
        
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        messages.success(self.request, "Logout Successful")
        return reverse_lazy('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        
        messages.success(self.request, "Profile updated Successfully")
        return render(request, self.template_name, {'form': form})
    
    
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/change_password.html'


    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        
        for field in form.fields.values():
            field.widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
    
        return form
    
    def form_valid(self, form):
       
        message = render_to_string('accounts/password_email.html', {
            'user' : self.request.user
        })
        

        messages.success(self.request, "Password updated Successfully")
        send_transaction_email(self.request.user, self.request.user.account.account_no, 'Password Changed Information', 'messages/passwordUpdate_email.html')
        return super().form_valid(form)
    

    def form_invalid(self, form):
        return super().form_invalid(form)


