%define major	4
%define libname	%mklibname xmp %{major}
%define devname	%mklibname xmp -d

Name:		libxmp
Summary:	Extended Module Player Library
Version:	4.6.0
Release:	1
# most of the source is LGPLv2+, exceptions:
# src/filter.c: MIT
# src/md5.*: Public domain
# src/fnmatch.*: BSD with advertising
# src/depackers/mmcmp.c: MIT
# src/depackers/ppdepack.c: Public domain
# src/depackers/unzoo.c: MIT
License:	BSD and LGPLv2+ and MIT and Public Domain
Group:		System/Libraries
Url:		https://xmp.sourceforge.net/
Source0:	http://download.sourceforge.net/xmp/%{name}-%{version}.tar.gz
BuildRequires:  locales-extra-charsets

%description
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

%package -n %{libname}
Summary:	Extended Module Player Library
Group:		System/Libraries

%description -n %{libname}
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	xmp-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -q

# non UTF-8 file
mv docs/Changelog docs/Changelog.old
iconv -f ISO-8859-1 -t UTF-8 -o docs/Changelog docs/Changelog.old

%build
%configure
%make_build

%install
%make_install

# man page
install -Dpm644 docs/libxmp.3 %{buildroot}%{_mandir}/man3/libxmp.3

# fix rights
chmod 755 %{buildroot}%{_libdir}/libxmp.so.*

%files -n %{libname}
%doc README docs/Changelog docs/CREDITS
%{_libdir}/libxmp.so.%{major}
%{_libdir}/libxmp.so.%{major}.*

%files -n %{devname}
%doc docs/libxmp.html docs/libxmp.pdf docs/*.txt
%{_includedir}/xmp.h
%{_libdir}/libxmp.so
%{_libdir}/pkgconfig/libxmp.pc
%{_libdir}/cmake/libxmp/
%{_mandir}/man3/libxmp.3.*

