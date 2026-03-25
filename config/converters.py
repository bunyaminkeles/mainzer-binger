"""
Özel URL path converter'ları.
"""
from django.core.cache import cache


class EyaletConverter:
    """
    Sadece veritabanındaki geçerli eyalet slug'larını eşleştirir.
    Bilinmeyen slug'lar (eski şehir URL'leri gibi) eşleşmez →
    fallback legacy-redirect patterns'e düşer.
    """
    regex = '[a-z][a-z0-9-]*'

    def to_python(self, value):
        valid = cache.get('_eyalet_slugs')
        if valid is None:
            from stadt.models import Eyalet
            valid = set(Eyalet.objects.values_list('slug', flat=True))
            cache.set('_eyalet_slugs', valid, 300)  # 5 dk cache
        if value in valid:
            return value
        raise ValueError

    def to_url(self, value):
        return value
