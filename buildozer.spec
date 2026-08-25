[app]
title = Spotify Ad-Cleaner
package.name = spotifyadcleaner
package.domain = org.adcleaner
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py
version = 1.0
requirements = python3,kivy,pillow
android.permissions = INTERNET,ACCESS_NETWORK_STATE
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1