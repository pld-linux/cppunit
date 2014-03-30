Summary:	The C++ Unit Test Library
Summary(pl.UTF-8):	Biblioteka testowa do C++
Name:		cppunit
Version:	1.13.2
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	d1c6bdd5a76c66d2c38331e2d287bc01
URL:		http://www.freedesktop.org/wiki/Software/cppunit/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%description -l pl.UTF-8
CppUnit jest portem C++ słynnego środowiska testowego JUnit.

%package devel
Summary:	cppunit header files
Summary(pl.UTF-8):	Pliki nagłówkowe cppunit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
cppunit header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe cppunit.

%package static
Summary:	cppunit static library
Summary(pl.UTF-8):	Statyczna biblioteka cppunit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
cppunit static library.

%description static -l pl.UTF-8
Statyczna biblioteka cppunit.

%package apidocs
Summary:	cppunit API documentation
Summary(pl.UTF-8):	Dokumentacja API cppunit
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
cppunit API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API cppunit.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# non-Linux
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/cppunit/{ui/mfc,ui/qt,config/config-{bcb5,evc4,mac,msvc6}.h}
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/cppunit/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/DllPlugInTester
%attr(755,root,root) %{_libdir}/libcppunit-1.13.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcppunit-1.13.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/FAQ
%attr(755,root,root) %{_bindir}/cppunit-config
%attr(755,root,root) %{_libdir}/libcppunit.so
%{_libdir}/libcppunit.la
%{_includedir}/cppunit
%{_aclocaldir}/cppunit.m4
%{_pkgconfigdir}/cppunit.pc
%{_mandir}/man1/cppunit-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcppunit.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
