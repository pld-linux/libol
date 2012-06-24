Summary:	libol
Summary(pl):	Biblioteka libol
Name:		libol
Version:	0.3.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.balabit.hu//downloads/syslog-ng/libol/0.3/%{name}-%{version}.tar.gz
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-gethostbyname_is_in_libc_aka_no_libnsl.patch
Patch2:		%{name}-AC_LIBOBJ.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libol is a small library used by syslog-ng, and provides
nonblocking-io, length encoded string functions and a mark & sweep
garbage collector.

%description -l pl
Libol jest niewielk� bibliotek� u�ywan� przez syslog-ng, a daj�c�
obs�ug� nieblokuj�cego wej�cia/wyj�cia, funkcje do obs�ugi ci�g�w
znak�w z zapisywan� d�ugo�ci� oraz od�miecacz.

%package devel
Summary:	Header files for libol
Summary(pl):	Pliki nag��wkowe do libol
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libol.

%description devel -l pl
Pliki nag��wkowe do libol.

%package static
Summary:	Static libol library
Summary(pl):	Biblioteka statyczna libol
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libol library.

%description static -l pl
Biblioteka statyczna libolo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/libol-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/libol

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
