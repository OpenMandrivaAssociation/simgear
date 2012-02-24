Name:		simgear
Version:	2.6.0
Release:	%mkrel 1
Summary:	Basic tools for Simulation
URL:		http://www.flightgear.org
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Source:		http://mirrors.ibiblio.org/pub/mirrors/simgear/ftp/Source/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	plib
BuildRequires:	zlib-devel
BuildRequires:	openal-devel
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

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files devel
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/*.a

