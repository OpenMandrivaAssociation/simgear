%define	name		simgear
%define	version		2.4.0
%define	release		%mkrel 1

Summary:	Basic tools for Simulation
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.flightgear.org
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://mirrors.ibiblio.org/pub/mirrors/simgear/ftp/Source/%{name}-%{version}.tar.bz2
BuildRequires:	plib
BuildRequires:  zlib-devel
BuildRequires:  openal-devel
BuildRequires:	libfreealut-devel
BuildRequires:	openscenegraph-devel
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
Provides:	lib%{name}-devel = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q

%build
%configure2_5x --disable-dependency-tracking

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files devel
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/*.a

