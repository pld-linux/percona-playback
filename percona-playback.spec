Summary:	A tool for replaying captured database server load
Name:		percona-playback
Version:	0.6
Release:	0.1
License:	GPL
Source0:	http://www.percona.com/downloads/Percona-Playback/LATEST/source/%{name}-%{version}.tar.gz
# Source0-md5:	d459f860052acfbad1c2c3d82cc62c25
Group:		Applications/Databases
URL:		http://www.percona.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
#BuildRequires:	libdrizzle-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtool
#BuildRequires:	mysql
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	tbb-devel
#Requires:	libdrizzle
#Requires:	libpcap
#Requires:	mysql
#Requires:	tbb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Percona Playback is a tool for replaying the captured load of one
database server against another in the most realistic way possible.
Captured load can come in the form of MySQL slow query logs or tcpdump
capture. It's multithreaded, modular and configurable to allow for
flexibility and future extension.

%package devel
Summary:	Development files for %{name}
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%{__sed} -i -e 's/AM_PROG_MKDIR_P/AC_PROG_MKDIR_P/' m4/po.m4
%{__sed} -i -e 's/mkdir_p/MKDIR_P/' po/Makefile.in.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/percona-playback
#%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
#%{_includedir}/*
#%{_libdir}/*.so
