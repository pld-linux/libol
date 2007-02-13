Summary:	libol library
Summary(pl.UTF-8):	Biblioteka libol
Name:		libol
Version:	0.3.18
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.balabit.hu/downloads/syslog-ng/libol/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	cbadf4b7ea276dfa85acc38a1cc5ff17
Patch0:		%{name}-autoconf.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libol is a small library used by syslog-ng, and provides
nonblocking-io, length encoded string functions and a mark & sweep
garbage collector.

%description -l pl.UTF-8
libol jest niewielką biblioteką używaną przez syslog-ng, a dającą
obsługę nieblokującego wejścia/wyjścia, funkcje do obsługi ciągów
znaków z zapisywaną długością oraz odśmiecacz.

%package devel
Summary:	Header files for libol
Summary(pl.UTF-8):	Pliki nagłówkowe do libol
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libol.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libol.

%package static
Summary:	Static libol library
Summary(pl.UTF-8):	Biblioteka statyczna libol
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libol library.

%description static -l pl.UTF-8
Biblioteka statyczna libol.

%package make_class
Summary:	libol make_class utility
Summary(pl.UTF-8):	Narzędzie make_class dla biblioteki libol
Group:		Development/Tools
Requires:	%{name}-devel = %{version}-%{release}

%description make_class
libol make_class development utility.

%description make_class -l pl.UTF-8
Narzędzie programistyczne make_class dla biblioteki libol.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SCSH=/bin/scsh
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libol.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libol-config
%attr(755,root,root) %{_libdir}/libol.so
%{_libdir}/libol.la
%{_includedir}/libol

%files static
%defattr(644,root,root,755)
%{_libdir}/libol.a

%ifnarch %{x8664} alpha ia64 s390x sparc64 ppc64
%files make_class
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/make_class
%endif
