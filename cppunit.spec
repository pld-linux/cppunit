Summary:	The C++ Unit Test Library
Summary(pl):	Biblioteka testowa do C++
Name:		cppunit
Version:	1.8.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/cppunit/%{name}-%{version}.tar.gz
# Source0-md5:	9f18d97ca99b4f095f5ff18139df59c3
URL:		http://cppunit.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%description -l pl
CppUnit jest portem C++ s³ynnego ¶rodowiska testowego JUnit.

%package devel
Summary:	cppunit header files
Summary(pl):	Pliki nag³ówkowe cppunit
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
cppunit header files.

%description devel -l pl
Pliki nag³ówkowe cppunit.

%package static
Summary:	cppunit static library
Summary(pl):	Statyczna biblioteka cppunit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
cppunit static library.

%description static -l pl
Statyczna biblioteka cppunit.

%prep
%setup -q

echo 'libcppunit_la_LIBADD = -lstdc++ -lpthread' >> src/cppunit/Makefile.am

%build
rm -f missing
%{__aclocal} -I config
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}/cppunit/{ui/mfc,ui/qt,config-[bm]*}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/FAQ doc/html
%attr(755,root,root) %{_bindir}/cppunit-config
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/cppunit
%{_aclocaldir}/cppunit.m4
%{_mandir}/man1/cppunit-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
