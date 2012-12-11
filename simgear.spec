Name:		simgear
Version:	2.8.0
Release:	%mkrel 1
Summary:	Basic tools for Simulation
URL:		http://www.flightgear.org
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries

Source:		http://mirrors.ibiblio.org/pub/mirrors/simgear/ftp/Source/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	plib
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(freealut)
BuildRequires:	pkgconfig(openscenegraph)
BuildRequires:	boost-devel

%description
All the basic routines required for the flight simulator as well as for
building scenery. Needed for FlightGear, for example.

%package devel
Summary:	Headers/misc for developing programs that will use %{name}
Group:		Development/C++
Obsoletes:	SimGear-devel
Provides:	SimGear-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q

%build
%cmake 
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%files devel
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/*.a

%changelog
* Mon Aug 20 2012 Anton Chernyshov <ach@rosalab.ru> 2.8.0-1
- New upstream release - 2.8.0

* Fri Feb 24 2012 Andrey Bondrov <abondrov@mandriva.org> 2.6.0-1
+ Revision: 780057
- New version 2.6.0, switch to cmake

* Wed Sep 21 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.0-3
+ Revision: 700648
- Rebuild

* Tue Sep 20 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.0-2
+ Revision: 700447
- Rebuild against new openscenegraph

* Sat Sep 17 2011 Andrey Bondrov <abondrov@mandriva.org> 2.4.0-1
+ Revision: 700084
- New version: 2.4.0

* Wed Jun 15 2011 Funda Wang <fwang@mandriva.org> 2.0.0-4
+ Revision: 685416
- rebuild

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2.0.0-3
+ Revision: 655816
- bunzip2 the patches

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2011.0
+ Revision: 614887
- the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Frederik Himpe <fhimpe@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 513660
- Update to new version 2.0.0
- Sync patches with Fedora
- Don't run autogen.sh but use autoreconf because the former does
  not work

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 1.9.1-2mdv2010.0
+ Revision: 419658
- fix installation

* Mon Mar 02 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.1-2mdv2009.1
+ Revision: 347580
- Apply ugly Fedora hack to fix pulling in simgear_config.h when
  HAVE_CONFIG_H is defined
  (https://bugzilla.redhat.com/show_bug.cgi?id=208678)
- Improve Provides of the devel package

* Mon Mar 02 2009 Frederik Himpe <fhimpe@mandriva.org> 1.9.1-1mdv2009.1
+ Revision: 347521
- Update to new version 1.9.1
- Build only dynamic libraries instead of static ones, create new
  lib package to contain libraries, and use the version as some kind
  of fake major
- Add Fedora patches
- Don't use rpath (Fedora)
- Improve linking (Fedora)
- Add openscenegraph and boost buildrequires
- Fix license
- Don't use -fno-omit-frame-pointer: it builds fine now without
  this flag with gcc 4.3

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 260675
- rebuild
- rebuild
- fix no-buildroot-tag

* Thu Dec 20 2007 Andreas Hasenack <andreas@mandriva.com> 1.0.0-1mdv2008.1
+ Revision: 135957
- updated to version 1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import simgear


* Sat Jul 29 2006 Bertrand Coconnier <bcoconni@hotmail.com> 0.3.10-3mdk
- Build for x86_64
- Remove dependency

* Thu Apr 20 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.3.10-2mdk
- Add BuildRequires

* Wed Apr 19 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3.10-1mdk
- 0.3.10

* Mon Nov 21 2005 Lenny Cartier <lenny@mandriva.com> 0.3.9-2mdk
- fix changelog

* Mon Nov 21 2005 Lenny Cartier <lenny@mandriva.com> 0.3.9-1mdk
- 0.3.9

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.8-1mdk
- 0.3.8

* Sat Oct 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.7-1mdk
- 0.3.7

* Thu Aug 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.6-1mdk
- 0.3.6
- fix buildrequires
- compile with Norman's jpeg image factory support

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.5-3mdk
- rebuild

* Tue Jun 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.5-2mdk
- rebuild

* Thu Apr 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.5-1mdk
- 0.3.5
- fix buildrequires (lib64..)

* Mon Oct 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.4-1mdk
- 0.3.4

* Wed Mar 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.1-4mdk
- rm -rf before makeinstall to make package short-circuitable..
- removed unneeded prefix macro

* Tue Mar 11 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.1-3mdk
- added zlib-devel to BuildRequires
- use a couple of macros for installing and building
- drop unapplied patch
- nicer formatting
- use mklibname macro

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-2mdk
- rebuild

* Thu Dec 19 2002  Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-1mdk
- 0.3.1

* Tue Sep 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.0-1mdk
- from Crispin Boylan <viewtronix@uklinux.net> :
	- new version

* Fri Sep 13 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.0.18-3mdk
- rebuild

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.18-2mdk
- recompile against latest libstdc++

* Mon Apr 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.18-1mdk
- new version

* Tue Feb 19 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.17-1mdk
- new version (using external zlib btw)
- true license is LGPL, not GPL

* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.16-2mdk
- lib policy
- fix invalid-spec-name simgear.spec
- fix obsolete-tag Copyright 

* Mon Jul 23 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.16-1mdk
- new version

* Fri Jun 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.15-2mdk
- rebuild against new plib

* Thu Jun 21 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.15-1mdk
- version 0.0.15

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.14-4mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Fri Mar  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.14-3mdk
- rebuild fix fixed plib

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.14-2mdk
- rebuild

* Wed Dec 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.14-1mdk
- 0.0.14 which is needed for latest FlightGear

* Tue Sep 26 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.13-1mdk
- 0.0.13 which is needed for latest FlightGear

* Tue Sep 26 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.12-2mdk
- simple rebuild

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.12-1mdk
- 0.0.12

* Thu Jun 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.10-1mdk
- first Mandrake Package

