# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global tunitas tu02
%global tunitas_dist %{?tunitas:.%{tunitas}}

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 1.8.4
Release: 3%{?tunitas_dist}%{?dist}
Name: tunitas-basics
Summary: Tunitas Audience Management System, basic components
License: Apache-2.0

Source0: %{name}-%{version}.tar.gz

BuildRequires: automake, autoconf, libtool, make
# We're going to go as close to C++2a as the compiler will allow.
BuildRequires: gcc-c++ >= 7.1.0
# But until ModulesTS is available S.C.O.L.D methodology is used.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Rich.2FBoolean_dependencies
# http://rpm.org/user_doc/boolean_dependencies.html
BuildRequires: (SCOLD-DC or anguish-answer >= 2.0 or baleful-ballad >= 0.17 or ceremonial-contortion or demonstrable-deliciousness)

BuildRequires: temerarious-flagship >= 1.3.0

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

%define module_nonstd_version 2:0.3.0
BuildRequires: module-nonstd-devel >= %{module_nonstd_version}
Requires:      module-nonstd >= %{module_nonstd_version}

%define module_options_version 0.14
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_posix_version 2:0.27.0
BuildRequires: module-posix-devel >= %{module_posix_version}
Requires:      module-posix >= %{module_posix_version}

%define module_std_version 2:0.27
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

%define module_string_version 0.13.1
BuildRequires: module-string-devel >= %{module_string_version}
Requires:      module-string >= %{module_string_version}

# the 'without' are by default enabled
# the 'with'    are by default disabled
%bcond_without make_check
%if %{with make_check}
%define module_rigging_unit_version 0.8.1
%define module_rigging_version      2:0.10.0
BuildRequires: (module-unit-rigging-devel >= %{module_rigging_unit_version} or module-rigging-devel >= %{module_rigging_version})
%endif

%description
Runtime libraries, files and other components of the Tunitas System.

%package devel
Summary: The development components of the Tunitas Audience Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++
Requires: module-httpserver-devel
Requires: module-nonstd-devel
Requires: module-options-devel
Requires: module-posix-devel
Requires: module-std-devel
Requires: module-string-devel

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas' are supplied.
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
    --enable-shared --enable-static \
    --prefix=%{_prefix} \
    --with-std-scold=%{std_scold_prefix} \
    --with-std-tunitas=%{std_tunitas_prefix} \
    --with-temerarious-flagship=%{std_tunitas_prefix} --with-FIXTHIS=this_should_not_be_needed_the_std_tunitas_should_be_sufficient \
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
# DO NOT mention directories or files that do not exist
%{_libdir}/*.so.*

%files devel
%doc ChangeLog README.md
# DO NOT mention directories or files that do not exist
%{modulesdir}/*
%exclude %dir %{modulesdir}/fpp
%exclude %dir %{modulesdir}/hpp
%exclude %dir %{modulesdir}/ipp
%{_libdir}/*
%exclude %{_libdir}/*.so.*
%exclude %{modulesdir}/want
%exclude %{modulesdir}/fpp/want
%exclude %{modulesdir}/hpp/want
%exclude %{modulesdir}/ipp/want

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Sun Sep 29 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.4-3
- The devel package MUST NOT take ownership of the %%{modulesdir}/{fpp,hpp,ipp} directories
- removed the tu02 particle from these change log entries (we already know it is tu02 %%tunitas_dist, just like we know it is %%dist)

* Wed Sep 18 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.4-2
- Be specific about the SCOLD-DC that is allowed, especially anguish-answer >= 2.0 or a recent baleful-ballad

* Fri Aug 23 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.4-1
- build robustification; portification to gcc 7

* Fri Aug 23 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.3-1
- copy in the new buildconf of temerarious-flagship >= 1.3.3

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.2-6
- MUST be built against nonstd-libhttpserver >= 0.9.0-7.1.ipv6+poll+regex+api else it will segfault at runtime
  MUST configure the build as such

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.2-5
- this MUST be built against nonstd-libhttpserver >= 0.9.0-7.1.ipv6+poll+regex+api else it will segfault at runtime
  and the configure MUST configure as such
- and require for testing module-rigging-devel >= 2:0.10.0
- do not declare ownership of the %%{modulesdir}/want directories

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.2-4
- copy in the buildconf from temerarious-flagship 1.3.1
- remind that in %%files, we cannot mention directories or files that do not exist
- MUST configure --with-temerarious-flagship so decorate with --with-FIXTHIS

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.1-3
- rachet into modern dependencies S.C.O.L.D. Ahead of Release 04 (Green Copper Heron), all in Epoch 2
- rachet to require temerarious-flagship >= 1.3, which is current for Tunitas Release 02 (Towering Redwood)

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.1-2
- second build for Release 02 (Towering Redwood)
- rachet the S.C.O.L.D. modules up to use the current Release 04 (Green Copper Heron) or the Tunitas Ahead builds of Epoch 2

* Mon Jul 15 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.1-1
- first build for Release 02 (Towering Redwood)
- disjunct for module-rigging-devel or module-rigging-unit-devel or module-unit-rigging-devel

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.2-1
- version and API sync among ChangeLog, configure.ac, src/tunitas/Makefrag.am

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.1-1
- install the modules of libtunitas
- removed mention of boost as it is not (yet) used.

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.0-2
- require temerarious-flagship-1.1.3 with --make-depend-script in .../am/compile.am

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.0-1
- first packaging, first release
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
