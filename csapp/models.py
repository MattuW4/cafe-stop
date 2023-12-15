from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

OPENING_HOURS = (
    (0, '12am'),
    (1, '1am'),
    (2, '2am'),
    (3, '3am'),
    (4, '4am'),
    (5, '5am'),
    (6, '6am'),
    (7, '7am'),
    (8, '8am'),
    (9, '9am'),
    (10, '10am'),
    (11, '11am'),
    (12, '12pm'),
    (13, '1pm'),
    (14, '2pm'),
    (15, '3pm'),
    (16, '4pm'),
    (17, '5pm'),
    (18, '6pm'),
    (19, '7pm'),
    (20, '8pm'),
    (21, '9pm'),
    (22, '10pm'),
    (23, '11pm'),
)


class Post(models.Model):
    """
    Database model for Posts
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="app_post")
    location = models.CharField(max_length=100)
    opening_time = models.IntegerField(max_length=2, choices=OPENING_HOURS, default=0)
    closing_time = models.IntegerField(max_length=2, choices=OPENING_HOURS, default=0)
    website = models.URLField(max_length=100, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        """Sets the order of posts by descending order"""
        ordering = ['-created_on']

    def __str__(self):
        """Returns string representation of object"""
        return self.title

    def number_of_likes(self):
        """Returns number of posts likes"""
        return self.likes.count()


class Comment(models.Model):
    """
    Database model for Comments
    """
    author = models.CharField(max_length=60)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Sets the order of posts by ascending order"""
        ordering = ['created_on']

    def __str__(self):
        """Returns the comment with body and name"""
        return f"Comment {self.body} by {self.author}"


class Category(models.Model):
    """
    Database model for Categories
    """
    name = models.CharField(max_length=30)

    class Meta:
        """Fixes incorrect category form from singular to plural"""
        verbose_name_plural = "categories"

    def __str__(self):
        """Returns the name of the category"""
        return self.name
