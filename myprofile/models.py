from django.db import models


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
        max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    relationship_status = models.CharField(
        max_length=100, null=True, blank=True)
    looking_for = models.CharField(
        max_length=100, null=True, blank=True)
    sexuality = models.CharField(
        max_length=50, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    body_type = models.CharField(max_length=50, null=True, blank=True)
    children = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    smoking = models.CharField(max_length=50, null=True, blank=True)
    drugs = models.CharField(max_length=50, null=True, blank=True)
    alcohol = models.CharField(max_length=50, null=True, blank=True)
    zodiac_sign = models.CharField(max_length=50, null=True, blank=True)

    pets = models.CharField(max_length=50, null=True, blank=True)

    political_views = models.CharField(max_length=50, null=True, blank=True)
    personality = models.CharField(max_length=50, null=True, blank=True)

    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    hair_color = models.CharField(max_length=50, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)

    position = models.CharField(max_length=50, null=True, blank=True)
    meet_at = models.CharField(max_length=50, null=True, blank=True)
    acceptnsfw = models.BooleanField(default=False)

    hiv_status = models.CharField(max_length=50, null=True, blank=True)
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
