Name:		socat
Summary:	Multipurpose relay
Version:	1.7.2.2
Release:	1
License:	GPL
Url:		http://www.dest-unreach.org/%{name}/
Group:		Networking/Remote access
Source0:	http://www.dest-unreach.org/%{name}/download/%{name}-%{version}.tar.gz
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
%doc README
%{_bindir}/%{name}
%{_bindir}/filan
%{_bindir}/procan
%{_mandir}/man1/*


%changelog
* Tue Dec 06 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.7.2.0-1
+ Revision: 738251
- version update 1.7.2.0

* Wed Sep 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.1.3-1mdv2011.0
+ Revision: 578480
- 1.7.1.3

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1.7.1.2-2mdv2010.1
+ Revision: 533646
- rebuild

* Thu Feb 11 2010 Frederik Himpe <fhimpe@mandriva.org> 1.7.1.2-1mdv2010.1
+ Revision: 504292
- update to new version 1.7.1.2

* Thu May 21 2009 Michael Scherer <misc@mandriva.org> 1.7.1.1-1mdv2010.0
+ Revision: 378364
- update to new version 1.7.1.1

* Fri Feb 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.0.0-2mdv2009.1
+ Revision: 345393
- rebuild against new readline

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 1.7.0.0-1mdv2009.1
+ Revision: 333005
- New upstream release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.6.0.0-4mdv2009.0
+ Revision: 242719
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 1.6.0.0-2mdv2008.0
+ Revision: 60856
- More buildrequires

* Sat May 26 2007 Emmanuel Blindauer <blindauer@mandriva.org> 1.6.0.0-1mdv2008.0
+ Revision: 31353
- 1.6.0.0 release
- Import socat

