#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libnotify
Version  : 0.8.1
Release  : 20
URL      : https://download.gnome.org/sources/libnotify/0.8/libnotify-0.8.1.tar.xz
Source0  : https://download.gnome.org/sources/libnotify/0.8/libnotify-0.8.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libnotify-bin = %{version}-%{release}
Requires: libnotify-data = %{version}-%{release}
Requires: libnotify-lib = %{version}-%{release}
Requires: libnotify-license = %{version}-%{release}
Requires: libnotify-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : xmlto

%description
# libnotify
## Description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the [org.freedesktop.Notifications][fdo-spec] Desktop
Specification. These notifications can be used to inform the user about an event
or display some form of information without getting in the user's way.

%package bin
Summary: bin components for the libnotify package.
Group: Binaries
Requires: libnotify-data = %{version}-%{release}
Requires: libnotify-license = %{version}-%{release}

%description bin
bin components for the libnotify package.


%package data
Summary: data components for the libnotify package.
Group: Data

%description data
data components for the libnotify package.


%package dev
Summary: dev components for the libnotify package.
Group: Development
Requires: libnotify-lib = %{version}-%{release}
Requires: libnotify-bin = %{version}-%{release}
Requires: libnotify-data = %{version}-%{release}
Provides: libnotify-devel = %{version}-%{release}
Requires: libnotify = %{version}-%{release}

%description dev
dev components for the libnotify package.


%package doc
Summary: doc components for the libnotify package.
Group: Documentation
Requires: libnotify-man = %{version}-%{release}

%description doc
doc components for the libnotify package.


%package lib
Summary: lib components for the libnotify package.
Group: Libraries
Requires: libnotify-data = %{version}-%{release}
Requires: libnotify-license = %{version}-%{release}

%description lib
lib components for the libnotify package.


%package license
Summary: license components for the libnotify package.
Group: Default

%description license
license components for the libnotify package.


%package man
Summary: man components for the libnotify package.
Group: Default

%description man
man components for the libnotify package.


%prep
%setup -q -n libnotify-0.8.1
cd %{_builddir}/libnotify-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658166125
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libnotify
cp %{_builddir}/libnotify-0.8.1/COPYING %{buildroot}/usr/share/package-licenses/libnotify/e60c2e780886f95df9c9ee36992b8edabec00bcc
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/notify-send

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Notify-0.7.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libnotify/notification.h
/usr/include/libnotify/notify-enum-types.h
/usr/include/libnotify/notify-features.h
/usr/include/libnotify/notify.h
/usr/lib64/libnotify.so
/usr/lib64/pkgconfig/libnotify.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libnotify/*
/usr/share/gtk-doc/html/libnotify/NotifyNotification.html
/usr/share/gtk-doc/html/libnotify/annotation-glossary.html
/usr/share/gtk-doc/html/libnotify/api-index-deprecated.html
/usr/share/gtk-doc/html/libnotify/api-index-full.html
/usr/share/gtk-doc/html/libnotify/ch01.html
/usr/share/gtk-doc/html/libnotify/home.png
/usr/share/gtk-doc/html/libnotify/index.html
/usr/share/gtk-doc/html/libnotify/left-insensitive.png
/usr/share/gtk-doc/html/libnotify/left.png
/usr/share/gtk-doc/html/libnotify/libnotify-notify.html
/usr/share/gtk-doc/html/libnotify/libnotify.devhelp2
/usr/share/gtk-doc/html/libnotify/right-insensitive.png
/usr/share/gtk-doc/html/libnotify/right.png
/usr/share/gtk-doc/html/libnotify/style.css
/usr/share/gtk-doc/html/libnotify/up-insensitive.png
/usr/share/gtk-doc/html/libnotify/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnotify.so.4
/usr/lib64/libnotify.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnotify/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/notify-send.1
