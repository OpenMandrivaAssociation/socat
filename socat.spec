Name:		socat
Summary:	Multipurpose relay
Version:	1.8.0.3
Release:	1
License:	GPL
Url:		https://www.dest-unreach.org/%{name}/
Group:		Networking/Remote access
Source0:	http://www.dest-unreach.org/%{name}/download/%{name}-%{version}.tar.gz
#Patch0:	09-fix_GCC10_FTBFS.patch
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(readline)
BuildRequires:	tcp_wrappers-devel

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/%{name}
%{_bindir}/socat-*.sh
%{_bindir}/socat1
%{_bindir}/filan
%{_bindir}/procan
%{_mandir}/man1/*
