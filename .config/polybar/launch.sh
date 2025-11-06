#!/bin/bash

# Polybar başlatma scripti

# Mevcut polybar işlemlerini sonlandır
killall -q polybar

# Polybar'ın tamamen kapanmasını bekle
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Polybar'ı başlat
polybar main &

echo "Polybar başlatıldı..."