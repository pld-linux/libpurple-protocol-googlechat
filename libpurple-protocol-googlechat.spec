%define		snap	20221106
%define		commit	b6b824a4764b51316f7be325492575684647e021
Summary:	Google Chat plugin for libpurple
Name:		libpurple-protocol-googlechat
Version:	0
Release:	0.%{snap}.1
License:	GPL v3+
Group:		Applications/Communications
Source0:	https://github.com/EionRobb/purple-googlechat/archive/%{commit}/purple-googlechat-%{commit}.tar.gz
# Source0-md5:	a75020095d2e2850532785d83281bede
URL:		https://github.com/EionRobb/purple-googlechat
BuildRequires:	glib2-devel
BuildRequires:	json-glib-devel
BuildRequires:	libpurple-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c
BuildRequires:	protobuf-c-devel
BuildRequires:	zlib-devel
Provides:	libpurple-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Google Chat plugin for libpurple.

%prep
%setup -qn purple-googlechat-%{commit}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/purple-2/libgooglechat.so
%{_pixmapsdir}/pidgin/protocols/*/googlechat.png
