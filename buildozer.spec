[app]
title = SimuladorFisica
package.name = simuladorfisica
package.domain = org.fisica
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
version = 0.1

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 0
