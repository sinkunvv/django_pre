from django.shortcuts import render
from hello.forms import InputForm
from hello.models import User

# Create your views here.
def index(request):
    message = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get('user_name')
            passwd = request.POST.get('passwd')

            if User.objects.filter(user_name=user_name, passwd=passwd).exists():
                message = 'ようこそ！' + user_name + 'さん'
            else:
                message = 'ユーザ名とパスワードが一致しません'
    else:
        form = InputForm()

    return render(request, "index.html", {'form': form, 'message': message})

def register(request):
    message = ''

    if request.method == 'POST':
        form  = InputForm(request.POST)
        if form.is_valid():
            user_name = request.POST.get('user_name')
            passwd = request.POST.get('passwd')

            try:
                user = User()
                user.user_name = user_name
                user.passwd = passwd
                user.save()
                message = user_name + "ようこそ！"

            except:
                message = 'すでに同じユーザ名が存在します'
        else:
                message = 'エラー'
    else:
        form = InputForm()

    return render(request, "register.html", {'form': form, 'message': message})
