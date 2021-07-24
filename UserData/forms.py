from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm

class MyAuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(MyAuthForm,self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = { 'autofocus': True,
                    'class' : 'form-control',
                    'id' : 'floatingInput',
                    'placeholder' : 'Username ไม่ต้องมี @email.com',
                    # 'placeholder' : 'RTAF email account ไม่ต้องมี @rtaf.mi.th',
                    'size' : 30}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'id' : 'floatingPassword'                                    
                    })
    )

class MyLoginView(LoginView):    
    authentication_form = MyAuthForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
 

class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm,self).__init__(*args, **kwargs)

    error_messages = {
        'password_mismatch': _('รหัสผ่านที่กรอกไม่เหมือนกัน'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("รหัสผ่านต้องยาวกว่า 8 ตัวอักษร และมีความซับซ้อนมากพอ"),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("ใส่รหัสผ่านซ้ำอีกครั้ง ให้เหมือนครั้งแรก"),
    )
