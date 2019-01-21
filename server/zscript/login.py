""" django 登录方式"""


"""
login():接受一个 HttpRequest对象和User 对象作为参数并使用Django的会话session框架把用户的ID保存在该会话中


_auth_user_hash
backend

    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
    request.session[BACKEND_SESSION_KEY] = backend
    request.session[HASH_SESSION_KEY] = session_auth_hash
    rotate_token # 刷新token
        user_logged_in.send(sender=user.__class__, request=request, user=user)

"""