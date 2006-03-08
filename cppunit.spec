Summary:	The C++ Unit Test Library
Summary(pl):	Biblioteka testowa do C++
Name:		cppunit
Version:	1.11.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/cppunit/%{name}-%{version}.tar.gz
# Source0-md5:	54734b1d054277e4fc0bac0df6e0aa4d
URL:		http://cppunit.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%description -l pl
CppUnit jest portem C++ słynnego środowiska testowego JUnit.

%package devel
Summary:	cppunit header files
Summary(pl):	Pliki nagłówkowe cppunit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
cppunit header files.

%description devel -l pl
Pliki nagłówkowe cppunit.

%package static
Summary:	cppunit static library
Summary(pl):	Statyczna biblioteka cppunit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
cppunit static library.

%description static -l pl
Statyczna biblioteka cppunit.

%prep
%setup -q

echo 'libcppunit_la_LIBADD = -ldl' >> src/cppunit/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}/cppunit/{ui/mfc,ui/qt,config/config-[bm]*}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/DllPlugInTester
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/FAQ doc/html
%attr(755,root,root) %{_bindir}/cppunit-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cppunit
%{_aclocaldir}/cppunit.m4
%{_pkgconfigdir}/cppunit.pc
%{_mandir}/man1/cppunit-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
