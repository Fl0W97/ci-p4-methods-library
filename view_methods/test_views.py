from django.contrib.auth.models import User  # Import the default User model
from django.test import TestCase
from django.urls import reverse
from .models import Method



class TestMethodFilteringViews(TestCase):

    def setUp(self):

        # Create a test user (since author is a ForeignKey to User)
        self.user = User.objects.create_user(username='testuser', password='password123')

    # Creating sample methods for testing
        self.method1 = Method.objects.create(
            title="Idea Generation Method",
            author=self.user,  # Assuming author is optional for testing
            purpose="Idea Generation",  # Matches the filter you want to test
            summary="A methodology to brainstorm ideas in a team",
            instructions="Step 1: Discuss, Step 2: Choose ideas...",
            material="Whiteboard, markers",
            prep_time="up to 10mins",
            duration="up to 10mins",
            alt_atr="Alternative method attribute",
            group_size_min=3,
            group_size_max=10,
            location="indoor",
            status=0,
            slug="idea-generation-method"
        )

        self.method2 = Method.objects.create(
            title="Collaboration Method",
            author=self.user,
            purpose="Collaboration",  # Different purpose
            summary="A methodology focused on improving collaboration",
            instructions="Step 1: Group activities...",
            material="Flip charts, pens",
            prep_time="up to 10mins",
            duration="up to 10mins",
            alt_atr="Different methodology attribute",
            group_size_min=4,
            group_size_max=12,
            location="outdoor",
            status=1,
            slug="collaboration-method"
        )

    def test_filter_methods_by_purpose(self):
        # Perform a GET request with the 'purpose' filter
        response = self.client.get(reverse('home'), {'purpose': 'Idea Generation'})

        # Assert that the response contains the expected method
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.method1.title)
        self.assertNotContains(response, self.method2.title)