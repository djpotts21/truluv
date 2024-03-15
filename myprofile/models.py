from django.db import models
import geoip2.webservice


# Get user location from geoip2
def get_location(ip):
    reader = geoip2.webservice.Reader('GeoLite2-City.mmdb')
    response = reader.city(ip)
    location = (
        response.city.name + ', ' +
        response.subdivisions.most_specific.name + ', ' +
        response.country.name
    )
    return location


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, default=0)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    bio = models.TextField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)
    image7 = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    pronouns = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(
        max_length=100, null=True, blank=True, editable=False)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    favorite_books = models.TextField(null=True, blank=True)
    favorite_movies = models.TextField(null=True, blank=True)
    favorite_music = models.TextField(null=True, blank=True)
    favorite_food = models.TextField(null=True, blank=True)
    favorite_drinks = models.TextField(null=True, blank=True)
    favorite_places = models.TextField(null=True, blank=True)
    relationship_status = models.CharField(
        max_length=20, null=True, blank=True)
    looking_for = models.TextField(null=True, blank=True)
    sexual_orientation = models.CharField(
        max_length=20, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    body_type = models.CharField(max_length=20, null=True, blank=True)
    children = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    smoking = models.CharField(max_length=20, null=True, blank=True)
    drugs = models.CharField(max_length=20, null=True, blank=True)
    alcohol = models.CharField(max_length=20, null=True, blank=True)
    zodiac_sign = models.CharField(max_length=20, null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    pets = models.TextField(null=True, blank=True)
    political_views = models.TextField(null=True, blank=True)
    personality = models.TextField(null=True, blank=True)
    education_level = models.CharField(max_length=20, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    tags = models.TextField(null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    ethnicity = models.CharField(max_length=20, null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    tribes = models.TextField(null=True, blank=True)
    looking_for_tribes = models.TextField(null=True, blank=True)
    meet_at = models.CharField(max_length=20, null=True, blank=True)
    acceptnsfw = models.BooleanField(default=False)
    hiv_status = models.CharField(max_length=20, null=True, blank=True)
    prep = models.BooleanField(default=False)
    last_tested = models.DateField(null=True, blank=True)
    vaccinations = models.TextField(null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    onlyfans = models.CharField(max_length=100, null=True, blank=True)
    snapchat = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.email
