%define	name	socat
%define version 1.7.2.0
%define release 1

Name:		%{name}
Summary:	Multipurpose relay
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://www.dest-unreach.org/%{name}/
Group:		Networking/Remote access
Source0:	http://www.dest-unreach.org/%{name}/download/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	openssl-devel ncurses-devel readline-devel tcp_wrappers-devel
Patch0:		unused_libs.patch

%description
socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_bindir}/filan
%{_bindir}/procan
%{_mandir}/man1/*
