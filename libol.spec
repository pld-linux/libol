Summary:	libol library
Summary(pl):	Biblioteka libol
Name:		libol
Version:	0.3.13
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.balabit.hu/downloads/syslog-ng/libol/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	b66e21769e21ac9b953cbafe517630fd
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-gethostbyname_is_in_libc_aka_no_libnsl.patch
Patch2:		%{name}-AC_LIBOBJ.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libol is a small library used by syslog-ng, and provides
nonblocking-io, length encoded string functions and a mark & sweep
garbage collector.

%description -l pl
libol jest niewielk± bibliotek± u¿ywan± przez syslog-ng, a daj±c±
obs³ugê nieblokuj±cego wej¶cia/wyj¶cia, funkcje do obs³ugi ci±gów
znaków z zapisywan± d³ugo¶ci± oraz od¶miecacz.

%package devel
Summary:	Header files for libol
Summary(pl):	Pliki nag³ówkowe do libol
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libol.

%description devel -l pl
Pliki nag³ówkowe do libol.

%package static
Summary:	Static libol library
Summary(pl):	Biblioteka statyczna libol
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libol library.

%description static -l pl
Biblioteka statyczna libol.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libol-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libol

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
