Summary:	LibASS - SSA/ASS subtitles rendering library
Name:		libass
Version:	0.10.0
Release:	1
License:	MIT-like
Group:		Libraries
#Source0Download: http://code.google.com/p/libass/downloads/list
Source0:	http://libass.googlecode.com/files/%{name}-%{version}.tar.xz
# Source0-md5:	1855bddc4c167f96968dddeeda0eb45c
URL:		http://code.google.com/p/libass/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enca-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	harfbuzz-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibASS is a portable subtitle renderer for the ASS/SSA (Advanced
Substation Alpha/Substation Alpha) subtitle format. It is mostly
compatible with VSFilter.


%description -l pl.UTF-8
LibASS to przenośna biblioteka renderująca napisy w formacie ASS/SSA
(Advanced Substation Alpha/Substation Alpha). Jest w większości
kompatybilna z VSFiltrem.

%package devel
Summary:	Header files for LibASS library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use LibASS library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changelog
%attr(755,root,root) %ghost %{_libdir}/libass.so.4
%attr(755,root,root) %{_libdir}/libass.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libass.so
%{_libdir}/libass.la
%{_includedir}/ass
%{_pkgconfigdir}/libass.pc

