from django.db import connection
from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great method'})

        """    #1 Save the form to trigger database queries (if any)
        comment_form.save()

        #2 After the query runs, print out all SQL queries executed
        print("SQL Queries executed during this test:")
        for query in TestCase.queries:
        print(query['sql'])    """

        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")
    
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")