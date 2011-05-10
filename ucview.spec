Name:		ucview
Version:	0.33
Release:	%mkrel 1
Summary:	A video capture and display program
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Url:		http://www.unicap-imaging.org/ucview.htm
License:	GPL
Group:		Video
BuildRequires:  dbus-glib-devel >= 0.73
BuildRequires:	libunicapgtk-devel >= 0.2.23
BuildRequires:	libGConf2-devel >= 2.22.0
BuildRequires:	libglade2-devel >= 2.6.2
BuildRequires:	gtk+2 >= 2.12.10
Requires(preun): GConf2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
UCView is a video capture and display program based on the unicap video imaging
library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas ucview

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/ucview.schemas
%{_datadir}/applications/ucview.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/icons/*
%{_datadir}/%{name}/logo/ucview-logo.png
%{_datadir}/%{name}/ucview.glade
%{_includedir}/%{name}/*
%{_bindir}/ucview
%{_libdir}/ucview/plugins/libhistogram.*
%{_datadir}/dbus-1/services/org.unicap-imaging.UCView.service
%{_mandir}/man1/ucview.1.*
