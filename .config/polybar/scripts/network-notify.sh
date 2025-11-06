#!/bin/bash
python3 ~/.config/polybar/scripts/network_speed.py --tooltip | xargs -I {} notify-send "{}"
