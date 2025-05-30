Summary:	GNOME Tour and Greeter
Summary(pl.UTF-8):	Przewodnik i powitanie środowiska GNOME
Name:		gnome-tour
Version:	48.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-tour/48/%{name}-%{version}.tar.xz
# Source0-md5:	e5b1e9524a797e29f9b7a43d244757e8
Patch0:		%{name}-no-update.patch
Patch1:		%{name}-x32.patch
URL:		https://gitlab.gnome.org/GNOME/gnome-tour
BuildRequires:	appstream-glib
BuildRequires:	cairo-devel >= 1.16
BuildRequires:	cargo
BuildRequires:	gdk-pixbuf2-devel >= 2.42
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.82
BuildRequires:	graphene-devel
BuildRequires:	gtk4-devel >= 4.16
BuildRequires:	libadwaita-devel >= 1
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.52.0
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	rust >= 1.70
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.16
Requires:	gdk-pixbuf2 >= 2.42
Requires:	glib2 >= 1:2.82
Requires:	gtk4 >= 4.16
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1
Requires:	pango >= 1:1.52.0
ExclusiveArch:	%{x8664} %{ix86} x32 aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debugsource packages don't support rust
%define		_debugsource_packages	0

%description
A guided tour and greeter for GNOME.

%description -l pl.UTF-8
Przewodnik i powitanie dla środowiska GNOME.

%prep
%setup -q
%patch -P0 -p1
%ifarch x32
%patch -P1 -p1
%endif

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson_install

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
%{_datadir}/gnome-tour
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml
%{_desktopdir}/org.gnome.Tour.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tour.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Tour-symbolic.svg
