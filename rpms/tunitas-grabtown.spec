%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 1.4.0
Release: 1
Name: tunitas-grabtown
Summary: Tunitas Audience Management, the DataX Compiler
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

# expect Epoch 1, the special build of Famous Oak (with modules of boost.program_options et al.)
%define module_boost_version 1:0.3.7
BuildRequires: module-boost-devel >= %{module_boost_version}
Requires:      module-boost >= %{module_boost_version}

# expect Epoch 1, the special build of Famous Oak (with types json::int64 et al.)
%define module_json_version 1:0.5.3
BuildRequires: module-json-devel >= %{module_json_version}
Requires:      module-json >= %{module_json_version}

%define module_options_version 1:0.13.0
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_sqlite_version 1:0.12.0
BuildRequires: module-sqlite-devel >= %{module_sqlite_version}
Requires:      module-sqlite >= %{module_sqlite_version}

%define module_std_version 1:0.25
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

%define module_sys_version 1:0.25
BuildRequires: module-sys-devel >= %{module_sys_version}
Requires:      module-sys >= %{module_sys_version}

%define module_rigging_version 1:0.8
# prefer rigging-unit (rigging-suite, rigging-bench) over the older unit-rigging nomenclature
BuildRequires: (module-rigging-unit-devel >= %{module_rigging_version} or module-unit-rigging-devel >= %{module_rigging_version})

%description
Runtime libraries, files and other components of Tunitas Tarwater, the Identity Management System.

%package devel
Summary: The development components of the Tunitas Tarwater Identity Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas::grabtown' are supplied.
These are "header files" and static & shared libraries.

%prep
%autosetup
make -i distclean >& /dev/null || : in case a devel tarball was used

%build
# with_module_boost=/build/tunitas/nearby/module-boost with_module_json=/build/tunitas/nearby/module-json with_hypogeal_twilight=/opt/scold with_nearby=no with_submodules=no ./maintenance/e2e
eval \
    prefix=%{_prefix} \
    with_temerarious_flagship=%{std_tunitas_prefix} \
    with_hypogeal_twilight=%{std_scold_prefix} \
    with_nearby=no \
    with_submodules=no \
    ./buildconf
%configure \
    --prefix=%{_prefix} \
    --without-submodules \
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
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc ChangeLog README.md
%{modulesdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.so.*
# These are supplied by tunitas-basics, because everyone has them.
%exclude %{modulesdir}/want
%exclude %{modulesdir}/ipp/want
%exclude %{modulesdir}/hpp/want
%exclude %{modulesdir}/fpp/want

%changelog
# DO NOT use ISO-8601 dates; only use date-abdY == $(date +'%%a %%b %%d %%Y')

* Fri Nov 09 2018  - Wendell Baker <wbaker@oath.com> - 1.4.0-1.tu01
- first packaging, first release as rpm
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
- deliver the development package with %%{modulesdir} and the module-want exclusions
