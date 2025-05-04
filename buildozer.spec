buildozer.spec for "Таблица Умножения"

[app]

(str) Title of your application

title = Таблица Умножения

(str) Package name (must be lowercase, no spaces)

package.name = tablica_umnozheniya

(str) Package domain (needed for android/ios packaging)

package.domain = org.test

(str) Source code where the main.py live

source.dir = .

(list) Source files to include (let empty to include all the files)

source.include_exts = py,png,jpg,kv,atlas

(str) Application versioning (method 1)

version = 0.1

(list) Application requirements

comma separated e.g. requirements = sqlite3,kivy

requirements = python3,kivy,random

(list) Supported orientations

orientation = portrait

(bool) Indicate if the application should be fullscreen or not

fullscreen = 0

(int) Target Android API, should be as high as possible.

android.api = 31

(int) Minimum API your APK will support.

android.minapi = 21

(int) Android SDK version to use (should match your installed SDK)

#android.sdk = 20

(str) Android NDK version to use

android.ndk = 21b

(int) Android NDK API to use (minimum API your app will support)

android.ndk_api = 21

(str) Android NDK directory (if empty, it will be automatically downloaded.)

#android.ndk_path =

(str) Android SDK directory (if empty, it will be automatically downloaded.)

#android.sdk_path =

(list) List of Android archs to build for

android.archs = arm64-v8a, armeabi-v7a

(bool) Copy library instead of making a libpymodules.so

#android.copy_libs = 1

(int) overrides automatic versionCode computation (used in build.gradle)

#android.numeric_version = 1

[buildozer]

(int) Log level (0 = error only, 1 = info, 2 = debug (with command output))

log_level = 2

(int) Display warning if buildozer is run as root (0 = False, 1 = True)

warn_on_root = 1

(str) Path to build output (i.e. .apk, .aab) storage

#bin_dir = ./bin



