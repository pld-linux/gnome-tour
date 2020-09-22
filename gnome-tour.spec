Summary:	GNOME Tour and Greeter
Summary(pl.UTF-8):	Przewodnik i powitanie środowiska GNOME
Name:		gnome-tour
Version:	3.38.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tour/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	b0c0bfe5806fdf31bbe840c464c6a479
URL:		https://gitlab.gnome.org/GNOME/gnome-tour
BuildRequires:	appstream-glib
BuildRequires:	cargo
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.64
BuildRequires:	gstreamer-devel >= 1.12
# pkgconfig(gstreamer-player-1.0)
BuildRequires:	gstreamer-plugins-bad-devel >= 1.12
# pkgconfig(gstreamer-video-1.0)
BuildRequires:	gstreamer-plugins-base-devel >= 1.12
BuildRequires:	gtk+3-devel >= 3.16
BuildRequires:	libhandy1-devel >= 1
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.64
Requires:	gstreamer >= 1.12
Requires:	gstreamer-plugins-bad >= 1.12
Requires:	gstreamer-plugins-base >= 1.12
Requires:	gtk+3 >= 3.16
Requires:	hicolor-icon-theme
Requires:	libhandy1 >= 1
ExclusiveArch:	%{x8664} %{ix86} x32 aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A guided tour and greeter for GNOME.

%description -l pl.UTF-8
Przewodnik i powitanie dla środowiska GNOME.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-tour
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml
%{_desktopdir}/org.gnome.Tour.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tour.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
