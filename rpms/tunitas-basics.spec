# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global tunitas tu02
%global tunitas_dist %{?tunitas:.%{tunitas}}

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 1.8.1
Release: 1%{?tunitas_dist}%{?dist}
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
BuildRequires: (SCOLD-DC or anguish-answer or baleful-ballad or ceremonial-contortion or demonstrable-deliciousness)

BuildRequires: temerarious-flagship >= 1.2.0

%define module_std_version 0.25
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

%define module_options_version 0.12
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

# Whereas the test rigging has migrated names as it has evolved
# but the underlying version numbering stays the same
%define module_rigging_version 0.8
BuildRequires: (module-rigging-devel >= %{module_rigging_version} or module-rigging-unit-devel >= %{module_rigging_version} or module-unit-rigging-devel >= %{module_rigging_version})

%description
Runtime libraries, files and other components of the Tunitas System.

%package devel
Summary: The development components of the Tunitas Audience Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++

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
    --with-temerarious-flagship=%{std_tunitas_prefix} \
    ${end}
%make_build \
    ${end}

%check
%make_build check

%install
%make_install

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc ChangeLog README.md
%{modulesdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.so.*

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Mon Jul 15 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.8.1-1.tu02
- first build of Release 02 (Towering Redwood)
- disjunct for module-rigging-devel or module-rigging-unit-devel or module-unit-rigging-devel

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.0.2-1
- version and API sync among ChangeLog, configure.ac, src/tunitas/Makefrag.am

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.0.1-1
- install the modules of libtunitas
- removed mention of boost as it is not (yet) used.

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-2
- require temerarious-flagship-1.1.3 with --make-depend-script in .../am/compile.am

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-1
- first packaging, first release
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
