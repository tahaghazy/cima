from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db import models

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class Category(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='categories')
    slug = models.SlugField(null=True,blank=True)
    post_update = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return f'/category/{self.slug}'


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Category,self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='posts')
    episode = models.IntegerField(default=1)
    image = models.ImageField(upload_to='posts')
    video = models.FileField(null=True,blank=True)
    embed = models.URLField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    post_update = models.DateTimeField(auto_now=True)
    post_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post,self).save(*args, **kwargs)



    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def FileURL(self):
        try:
            urll = self.video.url
        except:
            urll = ''
        return urll

    class Meta:
        ordering = ('-episode',)
        verbose_name = ('المنشور')
        verbose_name_plural = ('المنشورات')



