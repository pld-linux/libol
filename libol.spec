Summary:	libol
Summary(pl):	libol
Name:		libol
Version:	0.2.7
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://www.balabit.hu/products/syslog-ng/source/%{name}-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
Libol is a small library used by syslog-ng, and provides nonblocking-io,
length encoded string functions and a mark & sweep garbage collector.

%description -l pl
Libol jest niewielk± bibliotek± 

%package devel
Summary: 	Header files for libol 
Summary(pl):	Pliki nag³ówkowe do libol
Group: 		Development/Libraries
Group(pl): 	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files for libol.

%description -l pl devel
Pliki nag³ówkowe do libol.

%package static
Summary: 	Static libol library
Summary(pl):	Biblioteka statyczna libol
Group: 		Development/Libraries
Group(pl): 	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libol library.

%description -l pl static
Biblioteka statyczna libolo.

%prep
%setup -q

%build
%configure 

make 

gzip -9nf ChangeLog

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc ChangeLog.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libol-config
%{_libdir}/lib*.la
%{_includedir}/libol

%files static
%attr(644,root,root) %{_libdir}/lib*.a
