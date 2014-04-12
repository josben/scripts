
# Powered by SCESI

# Todo nacio de esto:
# debmirror --dry-run --verbose --postcleanup --method=http
# --host=ftp.br.debian.org --root=debian --dist=wheezy,jessie --arch=i386,amd64
# --section=main,contrib,non-free --nosource --no-check-gpg ./debmirror_tmp/
# | grep "Files to download""

method=http

arch=i386,amd64

section_debian=main,contrib,non-free
#section_ubuntu=main,restricted,universe,multiverse

dist=wheezy,wheezy-backports,wheezy-updates,wheezy-proposed-updates,jessie,jessie-backports,jessie-updates,jessie-proposed-updates
#dist=karmic,karmic-updates,karmic-security

server=ftp.us.debian.org

root=debian

# TODO: esto no se como se usa, al iniciar el script sale warnigns por el
# rsync y no logre entender ni se lo que hace, pero igual descarga.
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

