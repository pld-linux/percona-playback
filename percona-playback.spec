Summary:	A tool for replaying captured database server load
Name:		percona-playback
Version:	0.4
Release:	0.1
License:	GPL
URL:		http://www.percona.com/
Source0:	http://www.percona.com/downloads/Percona-Playback/Percona-Playback-%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	4cbe45401ee87a611d172301c13d4a4e
Group:		Applications/Databases
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
