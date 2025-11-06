#!/bin/bash
python3 ~/.config/polybar/scripts/weather.py --tooltip | xargs -I {} notify-send "Hava Durumu" "{}"
