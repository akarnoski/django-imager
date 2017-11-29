
"""Test module for imagersite."""
from bs4 import BeautifulSoup as soup

from django.contrib.auth.models import User
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse_lazy

# from imagersite.views import home_view


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """Create client to send requests."""
        self.client = Client()

    def test_home_view_status_code_200(self):
        """Test main view has 200 status."""
        response = self.client.get(reverse_lazy('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_has_title(self):
        """Test home page has h1 div with correct text."""
        response = self.client.get(reverse_lazy('homepage'))
        html = soup(response.content, 'html.parser')
        home = html.find('div', {'class': 'intro-lead-in'})
        self.assertIsNotNone(home)

    def test_home_page_inherits_base_template(self):
        """Test home page renders base.html template."""
        response = self.client.get(reverse_lazy('homepage'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_home_page_shows_login_link(self):
        """Test home page has login button."""
        response = self.client.get(reverse_lazy('homepage'))
        html = soup(response.content, 'html.parser')
        button = html.find('a', {'href': '/accounts/login'})
        self.assertIsNotNone(button)

    def test_login_view_status_code_301(self):
        """Test login view has 301 status."""
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)

    def test_login_view_renders_login_template(self):
        """Test login view has renders login template."""
        response = self.client.get('/accounts/login',
                                   follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_view_shows_input_box(self):
        """Test login view renders login input box."""
        response = self.client.get(reverse_lazy('login'),
                                   follow=True)
        html = soup(response.content, 'html.parser')
        login_name = html.find('input', {'name': 'username'})
        self.assertIsNotNone(login_name)

    def test_logging_in_with_nonexistent_user_goes_back_to_login_page(self):
        """Test login view has 200 status."""
        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'coyote',
                'password': 'allthepasswords'
            },
            follow=True
        )
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logging_in_with_user_redirects_to_home(self):
        """Test login view has 200 status."""
        user = User(username='coyote', email='coyote@coyote.com')
        user.set_password('allthepasswords')
        user.save()
        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'allthepasswords'
            },
            follow=True
        )
        self.assertTemplateUsed(response, 'imagersite/home.html')
        self.assertContains(response, bytes(user.username, 'utf8'))

    def test_logout_view_status_code_200(self):
        """Test logout view has 200 status."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_post_registration_redirects(self):
        """Test valid registation redirects to registration complete page."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            login_info
        )
        self.assertTrue(response.status_code, 302)
        self.assertTrue(response.url == reverse_lazy('registration_complete'))

    def test_post_registration_lands_on_reg_complete(self):
        """Test valid registration renders registration complete page."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            login_info,
            follow=True
        )
        self.assertContains(response, bytes(
            "To activate your account, please follow the link "
            "sent to the email you provided.", 'utf8'))

    def test_newly_registered_user_exists_and_is_inactive(self):
        """Test new account is not active."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            login_info,
            follow=True
        )
        self.assertTrue(User.objects.count() == 1)
        self.assertFalse(User.objects.first().is_active)

    def test_email_gets_sent_on_valid_registration(self):
        """Test email sent on valid registration."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            login_info,
            follow=True
        )
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Last step to activate your account.')
        content = mail.outbox[0].message().get_payload()
        self.assertTrue(content.startswith(
            'Thanks for registering your account with Imager.'))
        self.assertIn('coyote@coyote.com', email.to)

    def test_email_link_activates_account(self):
        """Test email link activates account."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            login_info,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n')[2]
        self.client.get(link)
        self.assertTrue(User.objects.count() == 1)
        user = User.objects.get(username='coyote')
        self.assertTrue(user.is_active)

    def test_activated_user_can_now_log_in(self):
        """Test if activated use can login."""
        login_info = {
            'username': 'coyote',
            'password1': 'allthepasswords',
            'password2': 'allthepasswords',
            'email': 'coyote@coyote.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            login_info,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n')[2]
        self.client.get(link)
        response = self.client.post(reverse_lazy('login'), {
            'username': 'coyote',
            'password': 'allthepasswords'
        },
            follow=True
        )
        self.assertContains(response, 'coyote')
