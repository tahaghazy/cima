from django.contrib.sitemaps import Sitemap
from .models import *
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.post_update

class CategorySitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.post_update



class StaticViewSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    def items(self):
        return ['home']
    def location(self, item):
        return reverse(item)