Name:		ucview
Version:	0.20.1
Release:	%mkrel 1
Summary:	A video capture and display program
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz

Url:		http://www.unicap-imaging.org/ucview.htm
License:	GPL
Group:		Video
BuildRequires:	libunicap-devel >= 0.2.23
BuildRequires:	libGConf2-devel >= 2.22.0
BuildRequires:	libglade2-devel >= 2.6.2
BuildRequires:	gtk+2 >= 2.12.10
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
 UCView is a video capture and display program based on the unicap video imaging library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

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
