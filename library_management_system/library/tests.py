from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Author

class AuthorTests(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.token = RefreshToken.for_user(self.user)
        self.access_token = str(self.token.access_token)
        
        # Create a test author
        self.author = Author.objects.create(
            name="Test Author",
            bio="This is a test bio."
        )
        
        self.url = '/authors/'  # The URL for the authors endpoint

    def test_get_authors(self):
        """Test the API endpoint to get a list of authors."""
        # Make GET request with Authorization header
        response = self.client.get(
            self.url,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}',
        )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the author created earlier is included in the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.author.name)
        
    def test_create_author(self):
        """Test the API endpoint to create a new author."""
        new_author_data = {
            "name": "New Author",
            "bio": "This is a new author bio."
        }
        
        # Make POST request to create new author
        response = self.client.post(
            self.url,
            new_author_data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}',
            format='json'
        )
        
        # Assert that the author is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the response contains the newly created author's data
        self.assertEqual(response.data['name'], new_author_data['name'])
        self.assertEqual(response.data['bio'], new_author_data['bio'])
        
        # Also check if the author is saved in the database
        author_in_db = Author.objects.get(id=response.data['id'])
        self.assertEqual(author_in_db.name, new_author_data['name'])
        self.assertEqual(author_in_db.bio, new_author_data['bio'])
