from django import forms


class InputForm(forms.Form):
    user_name = forms.CharField(required=True)
    passwd = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        # 半角英数字のみ
        if not user_name.encode('utf-8').isalnum():
            raise forms.ValidationError('ユーザ名は半角英数字のみです')
        return user_name

