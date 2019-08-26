# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

# install systemd unit files in /usr/lib/systemd no matter what %%{_prefix} says
%global systemd_systemdir  /usr/lib/systemd/system

Version: 0.0.4
Release: 1
Name: tunitas-tarwater
Summary: Tunitas Audience Management, the Identity Management System
License: Apache-2.0

Source0: %{name}-%{version}.tar.gz

BuildRequires: automake, autoconf, libtool, make
# We're going to go as close to C++2a as the compiler will allow.
BuildRequires: gcc-c++ >= 7.1.0
# But until ModulesTS is available S.C.O.L.D methodology is used.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Rich.2FBoolean_dependencies
# http://rpm.org/user_doc/boolean_dependencies.html
BuildRequires: (SCOLD-DC or anguish-answer or baleful-ballad or ceremonial-contortion or demonstrable-deliciousness)

BuildRequires: temerarious-flagship >= 1.3

# WATCHOUT - the use of Release:6 in the NEVR = tunitas-basics-1.8.2-6 is critical
#            because it is only at Release:6 that the basics were built against nonstd-libhttpserver >= 0.9.0-7.1.ipv6+poll+regex+api
#            without that, it will build, but you will get duplicate-free on exit ... mixing is unworkable.
%define tunitas_basics_version 1.8.2-6
BuildRequires: tunitas-basics-devel >= %{tunitas_basics_version}
Requires:      tunitas-basics >= %{tunitas_basics_version}

# requires currency beyond 04.green-copper-heron
# especially 2:0.2.2 which has cryptopp.byte to elide ::byte and CryptoPP::byte
%define module_crypto_version 2:0.2.2
BuildRequires: module-crypto-devel >= %{module_crypto_version}
Requires:      module-crypto >= %{module_crypto_version}

# the 'without' are by default enabled
# the 'with'    are by default disabled
%bcond_without nonstd_libhttpserver
%if %{with nonstd_libhttpserver}
# [[REMOVEWHEN]] taken care of as Recommends or Requires in module-httpserver.
# Those certain bugs in IPv6 port assignment are (incompletely) remediated.
# and yes, you do need all the patches for all those subystems
%define nonstd_libhttpserver_version 0.9.0-7.1.ipv6+poll+regex+api
%define nonstd_libhttpserver_prefix /opt/nonstd/libhttpserver
BuildRequires: nonstd-libhttpserver-devel >= %{nonstd_libhttpserver_version}
Requires:      nonstd-libhttpserver >= %{nonstd_libhttpserver_version}
%endif
%define module_httpserver_version 0.4
BuildRequires: module-httpserver-devel >= %{module_httpserver_version}
Requires:      module-httpserver >= %{module_httpserver_version}

# the 'without' are by default enabled
# the 'with'    are by default disabled
%bcond_with nonstd_jsoncpp
%if %{with nonstd_jsoncpp}
# Generally this is not warranted after jsoncpp-devel-1.7 era
%define nonstd_jsoncpp_version 1.7
%define nonstd_jsoncpp_prefix /opt/nonstd/jsoncpp
BuildRequires: nonstd-jsoncpp-devel >= %{nonstd_jsoncpp_version}
Requires:      nonstd-jsoncpp >= %{nonstd_jsoncpp_version}
%endif
# requires currency beyond 04.green-copper-heron
%define module_json_version 2:0.8.0
BuildRequires: module-json-devel >= %{module_json_version}
Requires:      module-json >= %{module_json_version}

# requires currency beyond 04.green-copper-heron
%define module_nonstd_version 2:0.3.0
BuildRequires: module-nonstd-devel >= %{module_nonstd_version}
Requires:      module-nonstd >= %{module_nonstd_version}

%define module_options_version 0.13
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_posix_version 2:0.27.0
BuildRequires: module-posix-devel >= %{module_posix_version}
Requires:      module-posix >= %{module_posix_version}

%define module_std_version 2:0.27.0
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

%define module_c_string_version 0.12.0
%define module_string_version   0.13.1
BuildRequires: (module-c-string-devel >= %{module_string_version} or module-string-devel >= %{module_string_version})
Requires:      (module-c-string >= %{module_string_version} or module-string >= %{module_string_version})

%define module_sys_version 2:0.27.0
BuildRequires: module-sys-devel >= %{module_sys_version}
Requires:      module-sys >= %{module_sys_version}

# the 'without' are by default enabled
# the 'with'    are by default disabled
%bcond_without make_check
%if %{with make_check}
%define module_rigging_unit_version 0.8.1
%define module_rigging_version      2:0.10.0
BuildRequires: (module-unit-rigging-devel >= %{module_rigging_unit_version} or module-rigging-devel >= %{module_rigging_version})
%endif

%description
Runtime libraries, files and other components of Tunitas Tarwater, the Identity Management System.

this is a reference implementation of the IAB Digi-Trust universal identity system.
It is an an application hosted within the httpserver which surface of GNU microhttpd.
As such, it is a "microervice" approach to delivering the identity linking function.

%package devel
Summary: The development components of the Tunitas Tarwater Identity Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++
Requires: tunitas-basics-devel
Requires: module-crypto-devel
Requires: module-httpserver-devel
Requires: module-json-devel
Requires: module-nonstd-devel
Requires: module-options-devel
Requires: module-posix-devel
Requires: module-std-devel
Requires: module-string-devel
Requires: module-sys-devel
Requires: module-sys-devel

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas::tarwater' are supplied.
These are "header files" and static & shared libraries.

%prep
%autosetup
make -i distclean >& /dev/null || : in case a devel tarball was used

%build
eval \
    prefix=%{_prefix} \
    with_temerarious_flagship=%{std_tunitas_prefix} \
    with_hypogeal_twilight=%{std_scold_prefix} \
    ./buildconf
%configure \
    --prefix=%{_prefix} \
    --with-std-scold=%{std_scold_prefix} \
    --with-std-tunitas=%{std_tunitas_prefix} \
    --with-temerarious-flagship=%{std_tunitas_prefix} \
    %{?with_nonstd_libhttpserver:--with-nonstd-libhttpserver=%{nonstd_libhttpserver_prefix}} \
    ${end}
%make_build \
    ${end}

%check
%make_build check

%install
%make_install

%files
%license LICENSE
%doc NEWS
%{_bindir}/*
%{_sbindir}/*
# NO DSO, only convenience libraries ---> %%{_libdir}/*.so.*
%{systemd_systemdir}/tarwater.service

%files devel
# Until the ChangeLog file is clearly no longer useful, it will be installed as documentation.
# The NEWS file contains Release Notes-type descriptions of the new features.
# The git log itself contains summarizations of the micro-level changes in the code.
%doc ChangeLog README.md
%if 0
#
# Towards the installation of the the development interface
# ... nothing is installed in the v0.0-series
# In the project Makefile.am, nearby
#    see lib_LIBRARIES
#    see modules_BB_SOURCES_ET
#
%{modulesdir}/*
%{_libdir}/*
# NO DSO, only convenience libraries ---> %%exclude %%{_libdir}/*.so.*
%exclude %{modulesdir}/want
%exclude %{modulesdir}/fpp/want
%exclude %{modulesdir}/hpp/want
%exclude %{modulesdir}/ipp/want
%endif

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Sun Aug 25 2019 - Wendell Baker <wbaker@verizonmedia.com> - 0.0.4-1
- and with %%{with make_check} enabled by default
- NEWS in lieu of ChangeLog going forward

* Sun Aug 25 2019 - Wendell Baker <wbaker@verizonmedia.com> - 0.0.3-1
- cram down the version number, back into the v0.0 series; semantic versioning
- portification back to Fedora 27, GCC 7, cryptopp-5.6.5 (with ::byte contra CryptoPP::byte)
- consistent installation of the DSOs (libraries) and the modules (header files)

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - <unavailable>0.0.2-2
- first build for Tunitas Release 02 (Towering Redwood)
- rachet to require temerarious-flagship >= 1.3, which is current for Tunitas Release 02 (Towering Redwood)
- and require for testing module-rigging-devel >= 2:0.10.0
- do not declare ownership of the %%{modulesdir}/want directories
- install systemd unit files in /usr/lib/systemd no matter what %%{_prefix} says

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - <unreleased>1.0.2-1
- synchronize API tokens and version badging

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - <unreleased>1.0.1-1
- ensure the -version-info $(CRA) gets into the libtunitas-tarwater.la link line.

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - <unreleased>1.0.0-1
- first packaging, first release.
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
