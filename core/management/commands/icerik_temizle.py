from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Süresi dolmuş ilanları, duyuruları ve eski forum konularını temizler'

    def handle(self, *args, **options):
        bugun = timezone.localdate()
        iki_ay_once = timezone.now() - timedelta(days=60)

        # Süresi dolan ilanları pasifleştir
        from ilan.models import Ilan
        ilan_sayisi = Ilan.objects.filter(
            aktif=True, yayin_bitis__lt=bugun
        ).update(aktif=False)
        self.stdout.write(f'{ilan_sayisi} ilan pasifleştirildi.')

        # Süresi dolan duyuruları yayından kaldır
        from duyurular.models import Duyuru
        duyuru_sayisi = Duyuru.objects.filter(
            yayinda=True, yayin_bitis__lt=bugun
        ).update(yayinda=False)
        self.stdout.write(f'{duyuru_sayisi} duyuru yayından kaldırıldı.')

        # 2 aydan eski forum konularını sil (sabitlenmişler hariç)
        from forum.models import Konu
        konu_sayisi, _ = Konu.objects.filter(
            sabitlendi=False, olusturulma__lt=iki_ay_once
        ).delete()
        self.stdout.write(f'{konu_sayisi} forum konusu silindi.')
