#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# İlk deploy: blog yazılarını ve seed verileri yükle
python blog_yazilari_ekle.py

# İlk deploy: RSS duyurularını çek
python manage.py rss_cek --sadece-rss || true
