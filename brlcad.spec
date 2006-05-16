#
# TODO - build with system libs: 
#
Summary:	BRL CAD
Summary(pl):	BRL CAD
Name:		brlcad
Version:	7.8.0
Release:	0.1
License:	GPL
Group:		Applications/CAD
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	bb4c5fd83ae1dd1b5dd84384f7894fc8
URL:		htp://brlcad.sourceforge.net/
#for TH
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libSM-devel
# for AC
#BuildRequires:	X11-devel
#
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
#Buildrequires:	itcl-devel
#BuildRequires:	itk-devel
Buildrequires:	python
BuildRequires:	SDL-devel
#BuildRequires:	tk-Img-devel

#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BRL-CAD package is a powerful Constructive Solid Geometry (CSG) solid modeling system with over 20 years development and production use by the U.S. military. BRL-CAD includes an interactive geometry editor, parallel ray-tracing support for rendering and geometric analysis, path-tracing for realistic image synthesis, network distributed framebuffer support, image-processing and signal-processing tools. The entire package is distributed in source code form.

%description -l pl

%package subpackage
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%package libs
Summary:	-
Summary(pl):	-
Group:		Libraries

%description libs

%description libs -l pl


%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

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
%{_mandir}/man?/*
%{_includedir}/*.h
%{_includedir}/brlcad
%{_libdir}/*
#%%{_libdir}/tk8.4
#%%{_libdir}/iwidgets4.0.1
%{_datadir}/%{name}


%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
