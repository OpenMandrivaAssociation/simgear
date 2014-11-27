Summary:	Basic tools for Simulation
Name:		simgear
Version:	3.2.0
Release:	2
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
Url:		http://www.flightgear.org
Source:		http://mirrors.ibiblio.org/pub/mirrors/simgear/ftp/Source/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	plib-devel
BuildRequires:	subversion-devel
BuildRequires:	pkgconfig(freealut)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openscenegraph)
BuildRequires:	pkgconfig(zlib)

%description
All the basic routines required for the flight simulator as well as for
building scenery. Needed for FlightGear, for example.

#----------------------------------------------------------------------------

%define libSimGearCore %mklibname SimGearCore %{version}

%package -n %{libSimGearCore}
Summary:	Shared library for SimGear
Group:		System/Libraries

%description -n %{libSimGearCore}
Shared library for SimGear.

%files -n %{libSimGearCore}
%{_libdir}/libSimGearCore.so.%{version}

#----------------------------------------------------------------------------

%define libSimGearScene %mklibname SimGearScene %{version}

%package -n %{libSimGearScene}
Summary:	Shared library for SimGear
Group:		System/Libraries

%description -n %{libSimGearScene}
Shared library for SimGear.

%files -n %{libSimGearScene}
%{_libdir}/libSimGearScene.so.%{version}

#----------------------------------------------------------------------------

%package devel
Summary:	Headers/misc for developing programs that will use SimGear
Group:		Development/C++
Requires:	%{libSimGearCore} = %{EVRD}
Requires:	%{libSimGearScene} = %{EVRD}
Conflicts:	%{_lib}SimGearCore3.0.0 < 3.2.0
Conflicts:	%{_lib}SimGearCore3.2.0 < 3.2.0-2

%description devel
This package contains the headers that programmers will need to develop
applications which will use SimGear, for example FlightGear.

%files devel
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/libSimGearCore.so
%{_libdir}/libSimGearScene.so
%{_datadir}/SimGearCore/SimGearCoreConfig-release.cmake
%{_datadir}/SimGearCore/SimGearCoreConfig.cmake

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake \
	-DJPEG_FACTORY:BOOL=ON \
	-DSYSTEM_EXPAT:BOOL=ON \
	-DSIMGEAR_SHARED:BOOL=ON
%make

%install
%makeinstall_std -C build
