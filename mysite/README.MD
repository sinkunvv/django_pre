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

```python

```