from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogYazisi
from rehber.models import Kaynak
from stadt.models import Stadt
from almanca.engine import konu_listesi


class StatikSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'core:anasayfa',
            'core:hakkinda',
            'core:iletisim',
            'almanca:liste',
        ]

    def location(self, item):
        return reverse(item)


class StadtSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Stadt.objects.filter(aktiv=True)

    def location(self, obj):
        return f'/{obj.slug}/'


class AlmancaSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return [k['slug'] for k in konu_listesi()]

    def location(self, slug):
        return reverse('almanca:quiz', kwargs={'slug': slug})


class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return BlogYazisi.objects.filter(yayinda=True, scope='eyalet')

    def lastmod(self, obj):
        return obj.olusturulma

    def location(self, obj):
        return reverse('rlp-blog:detay', kwargs={'slug': obj.slug})


class StadtBlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return BlogYazisi.objects.filter(yayinda=True, scope='stadt').select_related('stadt')

    def lastmod(self, obj):
        return obj.olusturulma

    def location(self, obj):
        if obj.stadt:
            return f'/{obj.stadt.slug}/blog/{obj.slug}/'
        return reverse('rlp-blog:detay', kwargs={'slug': obj.slug})


class RehberSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Kaynak.objects.filter(yayinda=True, scope='eyalet', tip='sayfa').exclude(slug=None).exclude(slug='')

    def lastmod(self, obj):
        return obj.guncelleme

    def location(self, obj):
        return reverse('rlp-rehber:detay', kwargs={'slug': obj.slug})


SITEMAPS = {
    'statik': StatikSitemap,
    'staedte': StadtSitemap,
    'almanca': AlmancaSitemap,
    'blog': BlogSitemap,
    'stadt-blog': StadtBlogSitemap,
    'rehber': RehberSitemap,
}
