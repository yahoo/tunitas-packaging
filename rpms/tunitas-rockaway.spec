# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 1.0.0
Release: 1
Name: tunitas-rockaway
Summary: Tunitas Audience Management, the DataX REST Service
License: Apache-2.0

Source0: %{name}-%{version}.tar.gz

BuildRequires: automake, autoconf, libtool, make
# We're going to go as close to C++2a as the compiler will allow.
BuildRequires: gcc-c++ >= 7.1.0
# But until ModulesTS is available S.C.O.L.D methodology is used.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Rich.2FBoolean_dependencies
# http://rpm.org/user_doc/boolean_dependencies.html
BuildRequires: (SCOLD-DC or anguish-answer or baleful-ballad or ceremonial-contortion or demonstrable-deliciousness)

BuildRequires: temerarious-flagship >= 1.1.3

%define tunitas_basics_version 1.0.1
BuildRequires: tunitas-basics-devel >= %{tunitas_basics_version}
Requires:      tunitas-basics >= %{tunitas_basics_version}

%define module_httpserver_version 0.4
BuildRequires: module-httpserver-devel >= %{module_httpserver_version}
Requires:      module-httpserver >= %{module_httpserver_version}

%bcond_without nonstd_libhttpserver
%if %{with nonstd_libhttpserver}
# [[REMOVEWHEN]] taken care of as Recommends or Requires in module-httpserver.
# Those certain bugs in IPv6 port assignment are (incompletely) remediated.
%define nonstd_libhttpserver_version 0.9.0-7.1.ipv6
%define nonstd_libhttpserver_prefix /opt/nonstd/libhttpserver
BuildRequires: nonstd-libhttpserver-devel >= %{nonstd_libhttpserver_version}
Requires:      nonstd-libhttpserver >= %{nonstd_libhttpserver_version}
%endif

%define module_options_version 0.12
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_std_version 0.25
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

%define module_rigging_version 0.8
BuildRequires: module-unit-rigging-devel >= %{module_rigging_version}

%description
Runtime libraries, files and other components of Tunitas Tarwater, the Identity Management System.

%package devel
Summary: The development components of the Tunitas Tarwater Identity Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas::rockaway' are supplied.
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
%{_sbindir}/*
%{_libdir}/*.so.*

%files devel
%doc ChangeLog README.md
# NOT YET ---> %%{modulesdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.so.*

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-1
- first packaging, first release
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
