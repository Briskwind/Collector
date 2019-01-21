from django.contrib.auth.backends import ModelBackend





class MyModelBackend(ModelBackend):
    """ 自定义后端认证"""