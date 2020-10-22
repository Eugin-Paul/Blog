from django.db import models

from django.contrib.auth.models import User

from tinymce import HTMLField


# class UserProfile(TimestampModel):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   picture = models.TextField(null=True, blank=True)


class Author(models.Model) :
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 200, null =True)
    profile_picture = models.ImageField(null = True, blank = True)
    picture = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def profileURL(self):
        try :
            url = self.profile_picture.url
        except :
            url = ''
        return url

class Category(models.Model):
    category_name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.category_name


class Post(models.Model) :
    title = models.CharField(max_length = 200, null = True)
    overview = models.TextField(max_length = 200,null = True)
    time_view = models.DateTimeField(auto_now_add = True,null = True)
    content = HTMLField(null = True)
    comment_count = models.IntegerField(default = 0, null = True)
    author = models.ForeignKey(Author,on_delete = models.SET_NULL, null = True)
    thumbnail = models.ImageField(null = True, blank = True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(null = True)

    def __str__(self):
        return self.title

    @property
    def thumbURL(self):
        try :
            url = self.thumbnail.url
        except :
            url = ''
        return url


class Comment (models.Model) :
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True)
    comment_post = models.TextField(max_length = 200,null = True)
    time_view = models.DateTimeField(auto_now_add = True,null = True)
    post = models.ForeignKey(Post,on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.comment_post
