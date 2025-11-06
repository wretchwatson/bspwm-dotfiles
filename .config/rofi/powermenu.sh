#!/bin/bash

# Rofi Power Menu

options="⏻ Kapat\n⟳ Yeniden Başlat\n⏾ Uyku\n🔒 Kilitle\n⎋ Çıkış"

chosen=$(echo -e "$options" | rofi -dmenu -i -theme-str 'window {width: 250px; location: northeast; anchor: northeast; x-offset: -10px; y-offset: 35px;} listview {lines: 5;} inputbar {enabled: false;}')

case $chosen in
    "⏻ Kapat")
        systemctl poweroff
        ;;
    "⟳ Yeniden Başlat")
        systemctl reboot
        ;;
    "⏾ Uyku")
        systemctl suspend
        ;;
    "🔒 Kilitle")
        i3lock -c 1b2224
        ;;
    "⎋ Çıkış")
        bspc quit
        ;;
esac