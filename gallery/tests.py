import pytest
from django.test import TestCase
from django.urls import reverse
from gallery.models import Category, Image
from gallery.views import gallery_view, image_detail
# Create your tests here.

def test_gallery_view(client):
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200

def test_image_detail_view(client):
    image = Image.objects.create(title='Test Image', category=Category, image_file='test.jpg')
    url = reverse('image_detail', kwargs={'pk': image.pk})
    response = client.get(url)
    assert response.status_code == 200