from django.test import TestCase
from gallery.models import Image
# Create your tests here.
class ModelImgTests(TestCase):
    def setup(self):
        Image.objects.create(title="Test", image='media/gallery_images/teddy.jpeg',
                             created_date="2023-05-20", age_limit=1, categories= 'Dogs')

    def test_get(self):
        img = Image.objects.get(title="Test")
        self.assertTrue(img)

    def test_age(self):
        img = Image.objects.get(title="Test")
        self.assertTrue(img.age_limit == 1)