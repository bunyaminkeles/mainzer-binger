from django.shortcuts import render, get_object_or_404
from .models import BlogYazisi

def liste(request):
    yazilar = BlogYazisi.objects.filter(yayinda=True)
    return render(request, 'blog/liste.html', {'yazilar': yazilar})

def detay(request, slug):
    yazi = get_object_or_404(BlogYazisi, slug=slug, yayinda=True)
    return render(request, 'blog/detay.html', {'yazi': yazi})
