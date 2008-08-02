%define	name		simgear
%define	oname		SimGear
%define	version		1.0.0
%define	release		%mkrel 4
%define	lib_name_orig	lib%{name}
%define	lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} %{lib_major} -d

Summary:	Basic tools for Simulation
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.simgear.org/
License:	LGPL
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		ftp://ftp.simgear.org/pub/simgear/Source/%{oname}-%{version}.tar.gz
Patch0:		SimGear-0.3.10-fix-x86_64.patch.bz2
BuildRequires:	autoconf2.5 
BuildRequires:  plib 
BuildRequires:  Mesa-common-devel 
BuildRequires:  zlib-devel 
BuildRequires:  openal-devel
BuildRequires:  jpeg-devel
BuildRequires:	libfreealut-devel
# Author: Curtis Olson <curt@flightgear.org>

%description
All the basic routines required for the flight simulator as well as for
building scenery. Needed for FlightGear, for example.

%package -n	%{lib_name_devel}
Summary:	Headers/misc for developing programs that will use %{name}
Group:		Development/C++
Obsoletes:	SimGear-devel
Provides:	SimGear-devel = %{version}-%{release} %{lib_name_orig}-devel = %{version}-%{release}

%description -n	%{lib_name_devel}
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
./autogen.sh

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
# (peroyvind) seems to build now:)
%configure --with-jpeg-factory
# (peroyvind) does'nt seem to handle several jobs, so don't use any macro
make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc README
%{_libdir}/*.*a
%{_includedir}/*

