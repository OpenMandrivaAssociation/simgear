%define	name		simgear
%define	oname		SimGear
%define	version		1.9.1
%define	release		%mkrel 1
%define	lib_major	%{version}
%define	lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} -d

Summary:	Basic tools for Simulation
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.simgear.org/
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		ftp://ftp.simgear.org/pub/simgear/Source/%{oname}-%{version}.tar.gz
Patch0:		SimGear-0.3.10-fix-x86_64.patch.bz2

# Fedora patches
Patch100:		SimGear-1.9.1-shared.patch
Patch101:		SimGear-1.9.0-notabbed_value_test.patch
Patch102:		SimGear-1.9.0-headers.patch
Patch105:		SimGear-1.9.1-untangle.patch
Patch107:		SimGear-1.9.0-more-archs.patch
Patch108:		SimGear-1.9.1-gcc44.patch

BuildRequires:	autoconf2.5
BuildRequires:	plib
BuildRequires:  Mesa-common-devel 
BuildRequires:  zlib-devel 
BuildRequires:  openal-devel
BuildRequires:  jpeg-devel
BuildRequires:	libfreealut-devel
BuildRequires:	openscenegraph-devel
BuildRequires:	boost-devel
# Author: Curtis Olson <curt@flightgear.org>

%description
All the basic routines required for the flight simulator as well as for
building scenery. Needed for FlightGear, for example.

%package -n %{lib_name}
Summary:	Basic tools for simulation
Group:		System/Libraries
Provides:	libsimgear = %{version}-%{release}

%description -n %{lib_name}
This package contains the libraries for applications that use
%{name},for example FlightGear.

%package -n %{lib_name_devel}
Summary:	Headers/misc for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	SimGear-devel
Obsoletes:	%mklibname %{name} -d 0
Provides:	%mklibname %{name} -d 0 = %{version}-%{release}
Provides:	SimGear-devel = %{version}-%{release} 
Provides:	simgear-devel = %{version}-%{release}
Provides:	libsimgear-devel = %{version}-%{release}

%description -n	%{lib_name_devel}
This package contains the headers that programmers will need to develop
applications which will use %{name}, for example FlightGear.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
# automake / autoconf input file changes
%patch100 -p1
# Have to disable the tabbed_value_test, because otherwise
# we get caught in a loop between libsgprops and libsgmisc.
%patch101 -p1
# Some circular dependcy fixing, see bz 208678
%patch105 -p1
# Fix compiling on pcc and alpha
%patch107 -p1
# Fix compiling with gcc44
%patch108 -p1
./autogen.sh

%build
# (peroyvind) seems to build now:)
%configure --with-jpeg-factory --disable-static
# Don't use rpath!   
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# We do not want -lm by default!
sed -i 's/ -lm / /g' libtool

# (peroyvind) does'nt seem to handle several jobs, so don't use any macro
make base_LIBS= openal_LIBS="-lalut -lopenal" \
  opengl_LIBS="-lglut -lGLU -lGL -lXmu -lXt -lSM -lICE -lXi -lXext -lX11"

%install
rm -rf %{buildroot}
%{makeinstall_std}
# Don't really need the .la files.
rm -rf %{buildroot}%{_libdir}/*.la

# These two headers have a useless conditional when they're not internal.
# This cleans them up.
cd %{buildroot}%{_includedir}/simgear/
patch -p0 < %{PATCH102}

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/lib*-%{version}.so

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS
%{_includedir}/simgear/
%{_libdir}/libsgbucket.so
%{_libdir}/libsgdebug.so
%{_libdir}/libsgenvironment.so
%{_libdir}/libsgephem.so
%{_libdir}/libsgio.so
%{_libdir}/libsgmagvar.so
%{_libdir}/libsgmaterial.so
%{_libdir}/libsgmath.so
%{_libdir}/libsgmisc.so
%{_libdir}/libsgmodel.so
%{_libdir}/libsgnasal.so
%{_libdir}/libsgprops.so
%{_libdir}/libsgroute.so
%{_libdir}/libsgscreen.so
%{_libdir}/libsgserial.so
%{_libdir}/libsgsky.so
%{_libdir}/libsgsound.so
%{_libdir}/libsgstructure.so
%{_libdir}/libsgtgdb.so
%{_libdir}/libsgthreads.so
%{_libdir}/libsgtiming.so
%{_libdir}/libsgutil.so
%{_libdir}/libsgxml.so

