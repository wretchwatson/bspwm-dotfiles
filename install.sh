#!/bin/bash

echo "=========================================="
echo "  BSPWM Dotfiles Kurulum Scripti"
echo "=========================================="
echo ""

# Root kontrolü
if [ "$EUID" -eq 0 ]; then 
    echo "Bu scripti root olarak çalıştırmayın!"
    exit 1
fi

# Paru kontrolü
if ! command -v paru &> /dev/null; then
    echo "Paru bulunamadı. Paru kuruluyor..."
    sudo pacman -S --needed base-devel git
    git clone https://aur.archlinux.org/paru.git /tmp/paru
    cd /tmp/paru
    makepkg -si --noconfirm
    cd -
else
    echo "Paru zaten kurulu."
fi

echo ""
echo "1. Resmi repo paketleri kuruluyor..."
sudo pacman -S --needed - < essential-packages.txt

echo ""
echo "2. AUR paketleri kuruluyor..."
paru -S --needed - < aur-packages.txt

echo ""
echo "3. Config dosyaları kopyalanıyor..."
cp -r .config/* ~/.config/
cp .Xresources ~/.Xresources
cp .gtkrc-2.0 ~/.gtkrc-2.0

echo ""
echo "4. SDDM config kopyalanıyor..."
sudo cp sddm.conf /etc/sddm.conf

echo ""
echo "5. Fontlar kopyalanıyor..."
sudo mkdir -p /usr/share/fonts/TTF
sudo cp -r fonts/Quicksand /usr/share/fonts/TTF/
sudo fc-cache -fv

echo ""
echo "6. Xorg monitor config kopyalanıyor..."
sudo mkdir -p /etc/X11/xorg.conf.d
sudo cp 10-monitor.conf /etc/X11/xorg.conf.d/10-monitor.conf

echo ""
echo "7. Dizinler oluşturuluyor..."
mkdir -p ~/Pictures/wallpapers

echo ""
echo "8. Servisler etkinleştiriliyor..."
sudo systemctl enable sddm
sudo systemctl enable NetworkManager

echo ""
echo "=========================================="
echo "  Kurulum tamamlandı!"
echo "=========================================="
echo ""
echo "Sistemi yeniden başlatın ve SDDM'den bspwm'i seçin."
echo ""
