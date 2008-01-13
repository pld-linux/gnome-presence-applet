Summary:	Presence applet from the Galago project
Summary(pl.UTF-8):	Aplet obecności z projektu Galago
Name:		gnome-presence-applet
Version:	0.3.1
Release:	1
License:	GPL (except for images - see COPYING)
Group:		X11/Applications
Source0:	http://www.galago-project.org/files/releases/source/gnome-presence-applet/%{name}-%{version}.tar.gz
# Source0-md5:	7527c126f72d0f5be083d9d9aa851e39
URL:		http://galago-project.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	libgalago-gtk-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Presence applet from the Galago project.

%description -l pl.UTF-8
Aplet obecności z projektu Galago.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only note about images
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
