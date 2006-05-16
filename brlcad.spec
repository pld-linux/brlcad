#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
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
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-DESTDIR.patch
URL:		htp://brlcad.sourceforge.net/
#BuildRequires:	-
#for TH
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libSM-devel
#
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Buildrequires:	itcl-devel
BuildRequires:	itk-devel
Buildrequires:	python
BuildRequires:	SDL-devel
BuildRequires:	tk-Img-devel
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
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
#%setup -q -c -T
#%setup -q -n %{name}
#%%setup -q -n %{name}-%{version}.orig -a 1
#%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

%build
#/autogen.sh
%configure \
    --disable-zlib-build \
    --disable-png-build \
    --disable-tcl-build \
    --disable-itcl-build \
    --disable-itk-build \
    --disable-tkimg-build
#{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
