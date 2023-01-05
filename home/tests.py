from django.test import TestCase
from rich import print
from django.conf import settings

# Create your tests here.
class HomeTest(TestCase):
    def test_check_running(self):
        """Test if there are any errors on the initial run
        """
        request = self.client.get("/")
        print("Debug:",settings.DEBUG)
        print("Status code:",request.status_code)