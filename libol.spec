Summary:	libol
Summary(pl):	libol
Name:		libol
Version:	0.2.5
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://www.balabit.hu/products/syslog-ng/source/%{name}-%{version}.tar.gz
#BuildRequires:	/bin/scsh
Buildroot:	/tmp/%{name}-%{version}-root

%description

%description -l pl

%package devel
Summary: 	libol-devel
Summary(pl):	libol-devel
Group: 		Development/Libraries
Group(pl): 	Programowanie/Biblioteki

%description devel

%description -l pl devel

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

%files
%defattr(644, root, root, 755)
%doc ChangeLog.gz
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libol-config
#%attr(755,root,root) %{_bindir}/make_class
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_includedir}/libol
