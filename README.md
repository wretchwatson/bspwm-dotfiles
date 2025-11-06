# BSPWM Dotfiles

Arch Linux için minimal ve temiz BSPWM masaüstü ortamı yapılandırması.

## Özellikler

- **Window Manager:** bspwm
- **Hotkey Daemon:** sxhkd
- **Compositor:** picom
- **Panel:** polybar
- **Launcher:** rofi
- **Bildirimler:** dunst
- **Terminal:** st
- **Dosya Yöneticisi:** pcmanfm-qt
- **Display Manager:** sddm
- **Tema:** Celestial Sea Dark

## Ekran Görüntüleri

*(Buraya ekran görüntüleri eklenebilir)*

## Kurulum

### Gereksinimler

- Arch Linux veya türevi (CachyOS önerilir)
- İnternet bağlantısı
- Git

### Kurulum Adımları

1. Repoyu klonlayın:
```bash
git clone <repo-url> ~/bspwm-dotfiles
cd ~/bspwm-dotfiles
```

2. Kurulum scriptini çalıştırın:
```bash
./install.sh
```

3. Sistemi yeniden başlatın:
```bash
reboot
```

4. SDDM'den bspwm'i seçin ve giriş yapın.

## Kısayollar

### Temel Kısayollar

- `Super + Return` - Terminal aç
- `Super + A` - Uygulama başlatıcı (rofi)
- `Super + Q` - Pencereyi kapat
- `Super + F` - Tam ekran
- `Alt + Tab` - Son iki workspace arasında geçiş

### Uygulama Kısayolları

- `Super + W` - Google Chrome
- `Super + E` - Dosya yöneticisi
- `Super + C` - VS Code

### Pencere Yönetimi

- `Super + H/J/K/L` - Pencere odaklama
- `Super + Shift + H/J/K/L` - Pencere taşıma
- `Super + Alt + H/J/K/L` - Pencere boyutlandırma

### Workspace Yönetimi

- `Super + 1-9,0` - Workspace'e geç
- `Super + Shift + 1-9,0` - Pencereyi workspace'e taşı

### Sistem

- `Super + Shift + E` - Çıkış
- `Super + Shift + R` - bspwm'i yeniden başlat
- `Super + Ctrl + R` - Polybar'ı yeniden başlat
- `Super + Shift + B` - Wallpaper değiştir

### Ses Kontrolleri

- `XF86AudioRaiseVolume` - Ses arttır
- `XF86AudioLowerVolume` - Ses azalt
- `XF86AudioMute` - Sesi kapat/aç

## Yapılandırma Dosyaları

- **bspwm:** `~/.config/bspwm/bspwmrc`
- **sxhkd:** `~/.config/sxhkd/sxhkdrc`
- **picom:** `~/.config/picom/picom.conf`
- **polybar:** `~/.config/polybar/config.ini`
- **rofi:** `~/.config/rofi/`
- **dunst:** `~/.config/dunst/`

## Özelleştirme

### Tema Değiştirme

GTK temaları için:
```bash
nwg-look
```

Qt temaları için:
```bash
qt6ct
```

### Wallpaper Ekleme

Wallpaper'larınızı `~/Pictures/wallpapers/` dizinine ekleyin.

### Polybar Özelleştirme

`~/.config/polybar/config.ini` dosyasını düzenleyin.

## Sorun Giderme

### Polybar görünmüyor
```bash
~/.config/polybar/launch.sh
```

### Kısayollar çalışmıyor
```bash
pkill -USR1 -x sxhkd
```

### Picom sorunları
```bash
pkill picom && picom &
```

## Notlar

- NVIDIA Optimus laptop'lar için optimus-manager yapılandırılmıştır
- Xorg monitor ayarları `/etc/X11/xorg.conf.d/10-monitor.conf` dosyasında
- SDDM teması Greenleaf olarak ayarlanmıştır

## Lisans

MIT

## Katkıda Bulunma

Pull request'ler kabul edilir. Büyük değişiklikler için önce bir issue açın.
