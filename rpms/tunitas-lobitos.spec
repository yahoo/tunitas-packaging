%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

%bcond_without nonstd_mysqlpp
%global nonstd_mysqlpp_prefix   /opt/nonstd/mysql++

Version: 1.0.2
Release: 1
Name: tunitas-lobitos
Summary: Tunitas Audience Management, the Audience Service
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

# expect Epoch 1, the front-running build of Famous Oak (with modules of apache.runtime et al..)
%define apache_httpd_api_version 1:0.2.0
BuildRequires: apache-httpd-api-devel >= %{apache_httpd_api_version}
Requires:      apache-httpd-api >= %{apache_httpd_api_version}

# expect Epoch 1, the front-running build of Famous Oak (with modules of boost.program_options et al.)
%define module_boost_version 1:0.3.7
BuildRequires: module-boost-devel >= %{module_boost_version}
Requires:      module-boost >= %{module_boost_version}

BuildRequires: module-format-devel
Requires:      module-format

BuildRequires: module-ish-devel
Requires:      module-ish

# expect Epoch 1, the front-running build of Famous Oak (with types json::int64 et al.)
%define module_json_version 1:0.5.3
BuildRequires: module-json-devel >= %{module_json_version}
Requires:      module-json >= %{module_json_version}

%define module_mysql_version 0.2.6
BuildRequires: module-mysql-devel >= %{module_mysql_version}
Requires:      module-mysql >= %{module_mysql_version}
%if %{with nonstd_mysqlpp}
%define nonstd_mysqlpp_version 3.2.3-14.1z.0
# WATCHOUT - the check in TF_CHECK_MYSQL looks for mysql++-devel independent of --with=nonstd+mysqlpp
#            so you have to build-require both nonstd-mysql++-devel AND ALSO mysql++-devel
# [[REMOVE WHEN]] temerarious-flagship TF_CHECK_MYSQL checks for EITHER nonstd-mysql++-devel OR mysql++-devel
BuildRequires: nonstd-mysql++-devel >= %{nonstd_mysqlpp_version}, mysql++-devel
Requires:      nonstd-mysql++ >= %{nonstd_mysqlpp_version}
%else
# Claimed: all problems fixed therein 3.2.4 since 2018-07-26
# Fedora 29 carries 3.2.4 (good)
# Fedora 28 carries 3.2.3 (avoid, use the nosn)
# Fedora 27 carries 3.2.3 (same)
# See https://tangentsoft.com/mysqlpp/doc/trunk/ChangeLog.md
%define std_mysqlpp_version 3.2.4 
BuildRequires: mysql++-devel >= %{std_mysqlpp_version}
Requires:      mysql++ >= %{std_mysqlpp_version}
%endif

%define module_options_version 1:0.13.0
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_std_version 1:0.25
BuildRequires: module-std-devel >= %{module_std_version}
Requires:      module-std >= %{module_std_version}

# prefer module-string (successor) over module-c-string (deprecating)
BuildRequires: (module-string-devel or module-c-string-devel)
Requires:      (module-string or module-c-string)

%define module_sys_version 1:0.25
BuildRequires: module-sys-devel >= %{module_sys_version}
Requires:      module-sys >= %{module_sys_version}

%define module_rigging_version 1:0.8
# prefer rigging-unit (rigging-suite, rigging-bench) over the older unit-rigging nomenclature
BuildRequires: (module-rigging-unit-devel >= %{module_rigging_version} or module-unit-rigging-devel >= %{module_rigging_version})

%description
Tunitas Lobitos is an incarnation of the DataX REST API. The package
contains runtime components for opeating the REST API.  Apache 2.4 is
supported as mod_audience

%package devel
Summary: The development components of the Tunitas Lobitos
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas::lobitos' are supplied.
These are "header files" and static & shared libraries.

%prep
%autosetup
make -i distclean >& /dev/null || : in case a devel tarball was used

%build
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
    --without-incendiary-sophist \
    --with-std-scold=%{std_scold_prefix} \
    --with-std-tunitas=%{std_tunitas_prefix} \
    --with-temerarious-flagship=%{std_tunitas_prefix} \
    %{?with_nonstd_mysqlpp:--with-nonstd-mysql++=%{nonstd_mysqlpp_prefix}} \
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

* Mon Nov 12 2018  - Wendell Baker <wbaker@oath.com> - 1.0.2-1.tu01
- first packaging, first release as rpm
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.
- deliver the development package with %%{modulesdir} and the module-want exclusions
