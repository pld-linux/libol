Summary:	libol
Summary(pl):	libol
Name:		libol
Version:	0.2.22
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.balabit.hu//downloads/syslog-ng/libol/0.2/%{name}-%{version}.tar.gz
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-gethostbyname_is_in_libc_aka_no_libnsl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libol is a small library used by syslog-ng, and provides
nonblocking-io, length encoded string functions and a mark & sweep
garbage collector.

%description -l pl
Libol jest niewielk± bibliotek± u¿ywan± przez syslog-ng.

%package devel
Summary:	Header files for libol 
Summary(pl):	Pliki nag³ówkowe do libol
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for libol.

%description -l pl devel
Pliki nag³ówkowe do libol.

%package static
Summary:	Static libol library
Summary(pl):	Biblioteka statyczna libol
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libol library.

%description -l pl static
Biblioteka statyczna libolo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/libol-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/libol

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
