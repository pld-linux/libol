Summary:	libol
Summary(pl):	libol
Name:		libol
Version:	0.2.0
Release:	2
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
#http:		www.balabit.hu
#path:		/products/syslog-ng/source
Source:		%{name}-%{version}.tar.gz
#BuildRequires:	/bin/scsh
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

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
./configure --prefix=%{_prefix} \
	--enable-shared \
	--enable-static \
	--disable-fast-install 

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" SCSH=/bin/sh

gzip -9 ChangeLog

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/%{name}*a
%attr(644,root,root) %{_includedir}/libol/*
%attr(755,root,root) %{_bindir}/libol-config
%attr(644,root,root) %{_bindir}/make_class

%files
%defattr(644, root, root, 755)
%doc ChangeLog.gz
%attr(644,root,root) %{_libdir}/%{name}.so*

%changelog
* Tue Jul 20 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [0.2.0-1]
- update to last version.

* Tue May  4 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [0.1.7-2]
- changing installation procedure,
- fixing requires problem.

* Wed Apr 28 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- build RPM.
