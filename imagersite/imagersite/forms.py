from registration.forms import RegistrationForm

from mycustomuserapp.models import MyCustomUser


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyCustomUser