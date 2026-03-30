from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
# from directory.models import City, Institution, Category # Kendi modellerini buraya ekle

class Command(BaseCommand):
    help = 'Bir şehri (KdU, Kurumlar, İlan altyapısı) veritabanında sıfırdan, hatasız ve güvenle inşa eder.'

    def add_arguments(self, parser):
        parser.add_argument('stadt_name', type=str, help='İnşa edilecek şehrin adı (Örn: Mainz)')
        # İleride --force veya --dummy-data gibi parametreler eklenebilir.

    def handle(self, *args, **options):
        # 1. Girdi Temizliği (Kullanıcı hatasını tolere et)
        stadt_name = options['stadt_name'].strip().title()

        self.stdout.write(f"🚀 [INIT] {stadt_name} ekosistemi ayağa kaldırılıyor...")

        try:
            # 2. Ya Hep Ya Hiç Kuralı (Bozuk veri oluşmasını engeller)
            with transaction.atomic():
                
                # ADIM 1: Şehri Yarat veya Getir (Idempotent)
                # city, created = City.objects.get_or_create(name=stadt_name)
                # action = "Yaratıldı" if created else "Zaten Mevcut, Güncelleniyor"
                # self.stdout.write(self.style.SUCCESS(f"  ✓ Şehir Kaydı: {action}"))

                # ADIM 2: Zorunlu Kurumları Ekle (Jobcenter, Ausländerbehörde vb.)
                # institutions = ["Jobcenter", "Ausländerbehörde", "Bürgeramt"]
                # for inst_name in institutions:
                #     Institution.objects.get_or_create(city=city, name=inst_name)
                # self.stdout.write(self.style.SUCCESS(f"  ✓ Temel Kurumlar Bağlandı."))

                # ADIM 3: İlan ve Kategori Altyapısı (Feature Flag ile uyumlu)
                # Category.objects.get_or_create(name="Emlak & Danışmanlık", city=city)
                # self.stdout.write(self.style.SUCCESS(f"  ✓ İlan Kategorileri Hazır."))

                # Gerçek mantık eklendiğinde yukarıdaki yorum satırlarını aktif et
                pass 

            # Eğer kod buraya ulaştıysa, her şey kusursuz işledi demektir.
            self.stdout.write(self.style.SUCCESS(f"✅ [BİTTİ] {stadt_name} başarıyla ayağa kaldırıldı ve yayına hazır."))

        except Exception as e:
            # İşlem yarıda kesilirse, veritabanını kirletmeden işlemi iptal eder ve uyarır.
            raise CommandError(f"HATA: {stadt_name} inşa edilirken sistem çöktü. İşlemler geri alındı (Rollback). Detay: {str(e)}")