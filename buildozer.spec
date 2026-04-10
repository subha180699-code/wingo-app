[app]
title = Wingo Predictor
package.name = wingoapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,pillow
orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a
android.api = 31
android.minapi = 21
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
