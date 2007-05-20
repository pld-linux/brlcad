#
# TODO 
#	- files fixes, what is -static?
#	- build with system libs: 
#
Summary:	BRL CAD - solid modeling system
Summary(pl.UTF-8):	BRL CAD - system modelowania brył
Name:		brlcad
Version:	7.8.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/brlcad/%{name}-%{version}.tar.bz2
# Source0-md5:	38854509545cb4a1b037d1ac47aac731
URL:		http://brlcad.sourceforge.net/
BuildRequires:	SDL-devel
#Buildrequires:	itcl-devel
#BuildRequires:	itk-devel
BuildRequires:	python
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
#BuildRequires:	tk-Img-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BRL-CAD package is a powerful Constructive Solid Geometry (CSG)
solid modeling system with over 20 years development and production
use by the U.S. military. BRL-CAD includes an interactive geometry
editor, parallel ray-tracing support for rendering and geometric
analysis, path-tracing for realistic image synthesis, network
distributed framebuffer support, image-processing and
signal-processing tools. The entire package is distributed in source
code form.

%description -l pl.UTF-8
BRL-CAD to potężny system modelowania brył CSG (Constructive Solid
Geometry) rozwijany i używany produkcyjnie od ponad 20 lat w
amerykańskim wojsku. BRL-CAD zawiera interaktywny edytor geometryczny,
obsługę równoległego ray-tracingu do renderowania i analizy
geometrycznej, path-tracing do realistycznej syntezy obrazu, obsługę
rozproszonego framebuffera po sieci oraz narzędzia do przetwarzania
obrazu i sygnału. Cały pakiet jest dostępny z kodem źródłowym.

%package devel
Summary:	Header files for BRL-CAD
Summary(pl.UTF-8):	Pliki nagłówkowe pakietu BRL-CAD
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for BRL-CAD.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe pakietu BRL-CAD.

%package static
Summary:	Static BRL-CAD library
Summary(pl.UTF-8):	Statyczna biblioteka BRL-CAD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static BRL-CAD library.

%description static -l pl.UTF-8
Statyczna biblioteka BRL-CAD.

%prep
%setup -q

%build
#/autogen.sh
%configure \
	--disable-blt-build \
	--disable-itcl-build \
	--disable-itk-build \
	--disable-png-build \
	--disable-regex-build \
	--disable-tcl-build \
	--disable-tkimg-build \
	--disable-zlib-build \
	--disable-debug \
	--disable-profiling \
	--enable-optimized \
	--with-gnu-ld \
	--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--datadir=%{_datadir} \
	--mandir=%{_mandir} \
	--sysconfdir=%{_sysconfdir}
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/*
#%%{_libdir}/tk7.4
#%%{_libdir}/iwidgets4.0.1
%{_datadir}/%{name}
%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/brlcad
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.la
