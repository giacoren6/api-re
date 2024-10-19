from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title= 'title, ')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_create_posts(self):
        response = self.client.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
 

class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(owner=adam, title='title', content='content adam')
        Post.objects.create(owner=brian, title='title', content='content brian')


def test_can_retrive_post_with_valid_id(self):
    response = self.client.get('/posts/1/')
    self.assertEqual(response.data['title'], 'title')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_cannot_retrive_post_with_invalid_id(self):
    response = self.client.get('/posts/999/')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


def test_logged_in_user_can_update_own_post(self):
    self.client.login(username='adam', password='pass')
    response = self.client.put('/posts/1/', {'title': 'new title',})
    posts = Post.objects.filter(pk=1).first()
    self.assertEqual(posts.title, 'new title')
    self.assertEqual(response.status_code, status.HTTP_200_OK)



def cannot_update_post_with_invalid_id(self):
    self.client.login(username='adam', password='pass')
    response = self.client.put('/posts/2/', {'title': 'new title'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





