#
# TODO 
#	- files fixes, what is -static?
#	- build with system libs: 
#
Summary:	BRL CAD - solid modeling system
Summary(pl):	BRL CAD - system modelowania bry�
Name:		brlcad
Version:	7.8.0
Release:	0.2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/brlcad/%{name}-%{version}.tar.bz2
# Source0-md5:	bb4c5fd83ae1dd1b5dd84384f7894fc8
URL:		http://brlcad.sourceforge.net/
#for TH
#BuildRequires:	xorg-lib-libICE-devel
#BuildRequires:	xorg-lib-libX11-devel
#BuildRequires:	xorg-lib-libXext-devel
#BuildRequires:	xorg-lib-libXi-devel
#BuildRequires:	xorg-lib-libXmu-devel
#BuildRequires:	xorg-lib-libXt-devel
#BuildRequires:	xorg-lib-libSM-devel
# for AC
BuildRequires:	XFree86-devel
#
BuildRequires:	SDL-devel
#Buildrequires:	itcl-devel
#BuildRequires:	itk-devel
BuildRequires:	python
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
#BuildRequires:	tk-Img-devel
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

%description -l pl
BRL-CAD to pot�ny system modelowania bry� CSG (Constructive Solid
Geometry) rozwijany i u�ywany produkcyjnie od ponad 20 lat w
ameryka�skim wojsku. BRL-CAD zawiera interaktywny edytor geometryczny,
obs�ug� r�wnoleg�ego ray-tracingu do renderowania i analizy
geometrycznej, path-tracing do realistycznej syntezy obrazu, obs�ug�
rozproszonego framebuffera po sieci oraz narz�dzia do przetwarzania
obrazu i sygna�u. Ca�y pakiet jest dost�pny z kodem �r�d�owym.

%package devel
Summary:	Header files for BRL-CAD
Summary(pl):	Pliki nag��wkowe pakietu BRL-CAD
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for BRL-CAD.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe pakietu BRL-CAD.

%package static
Summary:	Static BRL-CAD library
Summary(pl):	Statyczna biblioteka BRL-CAD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static BRL-CAD library.

%description static -l pl
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
#%%{_libdir}/tk8.4
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
