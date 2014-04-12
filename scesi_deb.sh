
method=http

arch=i386,amd64

section_debian=main,contrib,non-free
#section_ubuntu=main,restricted,universe,multiverse

dist=wheezy,jessie
#dist=karmic,karmic-updates,karmic-security

server=ftp.us.debian.org

root=debian

proto=rsync
rsyncoptions="-aIL --partial --bwlimit=100"

path=/opt/apps/tmp/mirror/debian/

debmirror --dry-run \
          --verbose \
          --postcleanup \
          --method=$method \
          --host=$server \
          --root=$root \
          --dist=$dist \
          -a $arch \
          --no-source \
          -s $section_debian \
          --no-check-gpg \
          --progress \
          --proxy=http://192.245.121.9:3128 \
          $path

