from django.db import connection
from django.test import TestCase
from .forms import CommentForm

""" Test comment form / Reused code from Code Institute
    see README.md credit section reused code """


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great method'})

        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
