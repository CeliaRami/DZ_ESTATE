from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
from properties.models import Property  # Ensure you import your Property model

@pytest.mark.django_db
def test_add_property_view(client, django_user_model):
    # Create a user
    user = django_user_model.objects.create_user(username="testuser", password="password123")
    client.login(username="testuser", password="password123")

    # Mock file upload with SimpleUploadedFile
    test_image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

    # POST request with form data and file
    response = client.post(reverse('add_property'), {
        'title': "Test Property",
        'description': "Test description",
        'price': 100000.00,
        'location': "Test City",
        'property_type': "house",
        'num_bedrooms': 2,
        'num_bathrooms': 1,
        'area': 120.0,
        'contact_info': "testuser@example.com",
        'photo': r"C:\Users\pc\Desktop\project 01\Abstract wallpaper by misia_bela - Download on ZEDGE™ _ c1f7.jpg"
  # Use the file object here
    })

    # Check if the response is a redirect (as expected after successful submission)
    assert response.status_code == 302  # Should redirect after successful submission
    
    # Check that a Property instance is created
    assert Property.objects.count() == 1
    
    # Check if the photo field is saved correctly
    # It will be saved in the 'property_photos' directory, you may need to adjust based on your settings
    assert Property.objects.first().photo.name.startswith("property_photos/test_image.jpg")
