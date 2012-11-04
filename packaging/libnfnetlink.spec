#
# spec file for package libnfnetlink
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           libnfnetlink
%define libsoname	%{name}
Version:        1.0.0+git28
Release:        2
License:        GPL-2.0
Url:            http://netfilter.org/projects/libnfnetlink/
Group:          Productivity/Networking/Security

Summary:        Low-level library for Netfilter-related kernel/userspace communication
#Git-Clone:	git://git.netfilter.org/libnfnetlink
#DL-URL:	ftp://ftp.netfilter.org/pub/libnfnetlink/
#Source:  %{name}-%{version}.tar.bz2
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake >= 1.6
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.23
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication. It provides a generic messaging
infrastructure for in-kernel netfilter subsystems (such as
nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) and their
respective users and/or management tools in userspace.

This library is not meant as a public API for application developers.
It is only used by other netfilter.org projects, such as
libnetfilter_log, libnetfilter_queue or libnetfilter_conntrack.

%package devel
Summary:        Low-level library for Netfilter-related kernel/userspace communication
Group:          Development/Libraries/C and C++
Requires:       %libsoname = %{version}

%description devel
libnfnetlink is the low-level library for netfilter related
kernel/userspace communication. It provides a generic messaging
infrastructure for in-kernel netfilter subsystems (such as
nfnetlink_log, nfnetlink_queue, nfnetlink_conntrack) and their
respective users and/or management tools in userspace.

This library is not meant as a public API for application developers.
It is only used by other netfilter.org projects, such as
libnetfilter_log, libnetfilter_queue or libnetfilter_conntrack.

%prep
%if 0%{?__xz:1}
%setup -q
%else
tar -xf "%{SOURCE0}" --use=xz;
%setup -DTq
%endif

%build
if [ ! -e configure ]; then
	autoreconf -fi;
fi
%configure --disable-static --includedir=%{_includedir}/%{name}-%{version}
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la;

%post -n %libsoname -p /sbin/ldconfig

%postun -n %libsoname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/libnfnetlink.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/libnfnetlink*
%{_libdir}/libnfnetlink.so
%{_libdir}/pkgconfig/libnfnetlink.pc

%changelog
