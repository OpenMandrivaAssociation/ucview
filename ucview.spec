Name:		ucview
Version:	0.33
Release:	3
Summary:	A video capture and display program
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Url:		https://www.unicap-imaging.org/ucview.htm
License:	GPLv2
Group:		Video
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.73
BuildRequires:	libunicapgtk-devel >= 0.2.23
BuildRequires:	pkgconfig(gconf-2.0) >= 2.22.0
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	gtk+2 >= 2.12.10
BuildRequires:	intltool GConf2
Requires(preun): GConf2
Patch0:		ucview-0.33-gmodule.patch

%description
UCView is a video capture and display program based on the unicap video imaging
library.

%prep
%setup -q
%patch0 -p1 -b .gmodule

%build
%configure2_5x --disable-schemas-install
%make

%install
%makeinstall_std
desktop-file-install --vendor "" --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
%find_lang %{name}

rm -fr %buildroot%_includedir %buildroot%_libdir/pkgconfig

%preun
%preun_uninstall_gconf_schemas ucview

%files -f %{name}.lang
%{_sysconfdir}/gconf/schemas/ucview.schemas
%{_datadir}/applications/ucview.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/icons/*
%{_datadir}/%{name}/logo/ucview-logo.png
%{_datadir}/%{name}/ucview.glade
%{_bindir}/ucview
%{_mandir}/man1/ucview.1.*
