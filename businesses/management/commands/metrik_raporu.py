from datetime import timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db.models import Count, DecimalField, ExpressionWrapper, F, Q, Sum
from django.utils import timezone

from businesses.models import LocalBusiness


class Command(BaseCommand):
    help = 'Yatırımcı sunumu için SaaS metrikleri: MRR, aktif işletme, churn oranı'

    def handle(self, *args, **options):
        today = timezone.localdate()
        thirty_days_ago = today - timedelta(days=30)

        # ── Aktif işletmeler ───────────────────────────────────────────────
        aktif_qs = LocalBusiness.objects.filter(
            is_published=True,
            end_date__gte=today,
        )
        aktif_sayisi = aktif_qs.count()

        # ── MRR ───────────────────────────────────────────────────────────
        # Her işletmenin aylık katkısı = plan_fiyat / duration_days * 30
        mrr_sonuc = (
            aktif_qs
            .filter(subscription_plan__isnull=False)
            .aggregate(
                mrr=Sum(
                    ExpressionWrapper(
                        F('subscription_plan__price')
                        / F('subscription_plan__duration_days')
                        * 30,
                        output_field=DecimalField(max_digits=10, decimal_places=2),
                    )
                )
            )
        )
        mrr = mrr_sonuc['mrr'] or Decimal('0')

        # Plan bazlı dağılım (tek sorgu)
        plan_dagilim = (
            aktif_qs
            .filter(subscription_plan__isnull=False)
            .values('subscription_plan__name', 'subscription_plan__price', 'subscription_plan__duration_days')
            .annotate(sayi=Count('id'))
            .order_by('-subscription_plan__price')
        )

        # ── Churn ─────────────────────────────────────────────────────────
        # Son 30 günde aboneliği biten ve yenilememiş işletmeler
        churned = LocalBusiness.objects.filter(
            end_date__gte=thirty_days_ago,
            end_date__lt=today,
        ).count()

        churn_base = aktif_sayisi + churned
        churn_rate = (churned / churn_base * 100) if churn_base else 0.0

        # ── Çıktı ─────────────────────────────────────────────────────────
        w = 48
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('═' * w))
        self.stdout.write(self.style.SUCCESS(f'  Almanyalı Rehber — SaaS Metrik Raporu'))
        self.stdout.write(self.style.SUCCESS(f'  {today.strftime("%d %B %Y")}'))
        self.stdout.write(self.style.SUCCESS('═' * w))

        self.stdout.write('')
        self.stdout.write(self.style.HTTP_INFO('  AKTİF İŞLETMELER'))
        self.stdout.write(f'  Toplam aktif          : {self.style.SUCCESS(str(aktif_sayisi))}')

        self.stdout.write('')
        self.stdout.write(self.style.HTTP_INFO('  AYLIK YİNELENEN GELİR (MRR)'))
        self.stdout.write(f'  MRR                   : {self.style.SUCCESS(f"€ {mrr:,.2f}")}')
        self.stdout.write(f'  Yıllık projeksiyon    : {self.style.SUCCESS(f"€ {mrr * 12:,.2f}")}')

        if plan_dagilim:
            self.stdout.write('')
            self.stdout.write(self.style.HTTP_INFO('  PLAN DAĞILIMI'))
            for p in plan_dagilim:
                aylik = (p['subscription_plan__price'] / p['subscription_plan__duration_days']) * 30
                self.stdout.write(
                    f"  {p['subscription_plan__name']:<22}"
                    f"  {p['sayi']:>3} işletme"
                    f"  (€{aylik:.0f}/ay)"
                )

        self.stdout.write('')
        self.stdout.write(self.style.HTTP_INFO('  CHURN (Son 30 Gün)'))
        self.stdout.write(f'  Aboneliği biten       : {churned}')

        churn_str = f'% {churn_rate:.1f}'
        if churn_rate == 0:
            self.stdout.write(f'  Churn oranı           : {self.style.SUCCESS(churn_str)}')
        elif churn_rate < 5:
            self.stdout.write(f'  Churn oranı           : {self.style.WARNING(churn_str)}')
        else:
            self.stdout.write(f'  Churn oranı           : {self.style.ERROR(churn_str)}')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('═' * w))
        self.stdout.write('')
