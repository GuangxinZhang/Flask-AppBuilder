from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.views import UserInfoEditView

from .models import MyUser
from .sec_views import MyUserDBModelView
from .sec_forms import UserInfoEdit


class MyUserInfoEditView(UserInfoEditView):
    form = UserInfoEdit


class MySecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView
    userinfoeditview = MyUserInfoEditView
