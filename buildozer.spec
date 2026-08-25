[app]

# (str) Title of your application
title = Spotify Ad-Cleaner

# (str) Package name
package.name = spotifyadcleaner

# (str) Package domain (needed for android packaging)
package.domain = org.adcleaner

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Directory where the source files are located
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pillow

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# --- إعدادات الإصدارات لتجاوز مشكلة التراخيص و Aidl ---
android.api = 31
android.min_api = 21
android.sdk = 30
android.ndk = 23b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
