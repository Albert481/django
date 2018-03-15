from accounts.models import Auth_User

class SettingsBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Auth_User.objects.get(email=username)
            if user.check_password(password):
                return user
        except Auth_User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Auth_User.objects.get(pk=user_id)
            if user.is_active:
                return user
        except Auth_User.DoesNotExist:
            return None