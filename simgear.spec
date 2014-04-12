# It's empty here anyway
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		simgear
Version:	3.0.0
Release:	1
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
BuildRequires:	pkgconfig(glu)
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	subversion-devel

%description
All the basic routines required for the flight simulator as well as for
building scenery. Needed for FlightGear, for example.

%package devel
Summary:	Headers/misc for developing programs that will use %{name}
Group:		Development/C++
Provides:	SimGear-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q

%build
%cmake -DJPEG_FACTORY:BOOL=ON
%make

%install
%makeinstall_std -C build

%files devel
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/*.a

