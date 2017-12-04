from imager_profile.models import ImagerProfile


class ImagerUserForm(RegistrationForm):
    Class Meta:
        model = ImagerProfile
