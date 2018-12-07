# でじゃんご勉強会用リポジトリ

* 2018/12/08
* Geek鯖(笑)3.0.1
* Speaker しんくん

## 解説用スライド
https://docs.google.com/presentation/d/1KmsnJLvOLi4OsD_MT3LUnJA2xsWTpLxyXm7gKDos8io/edit?usp=sharing

## 補足モデル操作
    同じようなフォームを用意するのがしんどくなったので
    UpdateとDeleteの操作はここで

## Update

```python
    user = User.objects.get(user_name=user_name)
    user.passwd = '新しいパスワード'
    user.save()
```

## Delete

```python
    user = User.objects.get(user_name=user_name)
    user.delete()
```

## ForeignKey(1対多の外部キー制約)

ユーザに対してタスクがリレーションを張る
```python
    class User(models.Model):
        user_name = CharField()
        passwd = CharField()

    class Task(models.Model):
        task_name = TextField()
        user = ForeignKey(User, on_delete=models.CASCADE, related_name='task')
```

ユーザに対してリレーションしているタスクを逆参照して全取得をかける
```python
    user = User.objects.get(user_name=user_name)
    task = user.task.all()
```

## OneToOneField(1対1の外部キー制約)

ユーザに対してプロフィールが1対1になるようにリレーションを張る
```python
    class User(models.Model):
        user_name = CharField()

    class Profile(models.Model):
        profile = TextField()
        user = OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
```

```python
    user = User.objects.get(user_name=user_name)
    profile = user.profile
```
