from django.contrib.auth.models import User  # Import the default User model
from django.test import TestCase
from django.urls import reverse
from .forms import CommentForm
from .models import Method


class TestMethodViews(TestCase):

    # Create a test user (since author is a ForeignKey to User)
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
        )

        # Creating sample methods for testing
        self.method = Method(
            title="Test title", author=self.user,
            slug="test-title", purpose="Idea Generation",
            summary="Test summary", instructions="Test instructions",
            material="Test material", prep_time="up to 10mins",
            duration="up to 10mins", alt_atr="Test alt_atr",
            group_size_min=3, group_size_max=10,
            location="indoor", status=1
        )
        self.method.save()

    def test_render_method_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'method_page', args=['test-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test title", response.content)
        self.assertIn(b"Test instructions", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)


class TestMethodFilteringViews(TestCase):

    def setUp(self):

        # Create a test user (since author is a ForeignKey to User)
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )

    # Creating sample methods for testing
        self.method1 = Method(
            title="Test title", author=self.user,
            slug="test-title", purpose="Idea Generation",
            summary="Test summary", instructions="Test instructions",
            material="Test material", prep_time="up to 10mins",
            duration="up to 10mins", alt_atr="Test alt_atr",
            group_size_min=3, group_size_max=10,
            location="indoor", status=1
        )

        self.method2 = Method(
            title="Collaboration Method", author=self.user,
            slug="test-title", purpose="Conflict resolution",
            summary="Test summary", instructions="Test instructions",
            material="Test material", prep_time="up to 10mins",
            duration="up to 10mins", alt_atr="Test alt_atr",
            group_size_min=4, group_size_max=12,
            location="outdoor", status=1
            )


    def test_filter_methods_by_purpose(self):
        # Perform a GET request with the 'purpose' filter
        response = self.client.get(
            reverse('home'), {'purpose': 'Idea Generation'}
        )

        # Assert that the response contains the expected method
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.method1.purpose)
        self.assertNotContains(response, self.method2.purpose)
