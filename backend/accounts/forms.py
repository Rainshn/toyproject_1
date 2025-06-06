from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': _('아이디'),
            'password1': _('비밀번호'),
            'password2': _('비밀번호 확인'),
        }
        help_texts = {
            'username': _('아이디를 입력해주세요.'),
            'password1': _('비밀번호를 입력해주세요.'),
            'password2': _('비밀번호 확인을 입력해주세요.'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '아이디를 입력하세요'}),
            'password1': forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요'}),
            'password2': forms.PasswordInput(attrs={'placeholder': '비밀번호를 다시 입력해주세요'}),
        }
        error_messages = {
            'username': {
                'required': _('아이디는 필수 항목입니다.'),
                'max_length': _('아이디는 30자 이내여야 합니다.'),
            },
            'password1': {
                'required': _('비밀번호는 필수 항목입니다.'),
            },
            'password2': {
                'required': _('비밀번호 확인은 필수 항목입니다.'),
            }
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            if len(password1) < 8 or len(password1) > 16:
                raise forms.ValidationError(_('비밀번호는 8~16자를 입력해주세요.'))
        return password1