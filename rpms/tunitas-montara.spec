# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

# install systemd unit files in /usr/lib/systemd no matter what %%{_prefix} says
%global systemd_systemdir  /usr/lib/systemd/system

#
# [[FIXTHIS]] many of these southside schemes are not yet possible in montara; they flow over from apanolio
# All of these may be used simultaneously; they are further enabled at configure time.
# Build the service with 
# rpmbuild --with=NAME --with=NAME ...etc...
# mock --with=NAME --with=NAME ...etc...
#
#   --with=southside_fabric           The "southside" storage backend can be Hyperledger Fabric
#   --with=southside_leveldb          The southside can be  a filesystem-local LevelDB
#   --with=southside_sqlite           The southside can be  a filesystem-local SQLite
#   --with=southside_mysql            The southside can be a nearby MySQL
#   --with=southside_pgsql            The southside can be a nearby PostgreSQL (PgSQL)
#   --with=southside_ramcloud         The southside can be a nearby RAMCloud
#   --with=southside_scarpet          Tunitas has the DID Identity Systems (Hipster, Philosophical, Elemental, etc.)
#
# Recall (via /usr/lib/rpm/macros)
#
#    %%bcond_with foo       defines symbol with_foo if --with foo was specified on command line.
#    %%bcond_without foo    defines symbol with_foo if --without foo was *not* specified on command line.
#
# i.e. the 'without' are by default enabled
#      the 'with'    are by default disabled
#
%bcond_with    southside_fabric
%bcond_without southside_leveldb
%bcond_without southside_mysql
%bcond_with    southside_pgsql
%bcond_without southside_sqlite
%bcond_with    southside_ramcloud
%bcond_with    southside_scarpet

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 0.1.2
Release: 1
Name: tunitas-montara
Summary: Tunitas microservice of the "Northbound API Service" for the IAB PrivacyChain
License: Apache-2.0

Source0: %{name}-%{version}.tar.gz

BuildRequires: automake, autoconf, libtool, make
# We're going to go as close to C++2a as the compiler will allow.
# So consider using gcc 9.1
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

%define tunitas_butano_version 1.0.0
BuildRequires: tunitas-butano-devel >= %{tunitas_butano_version}
Requires:      tunitas-butano >= %{tunitas_butano_version}

%if %{with southside_fabric}
%define hyperledger_fabric_version 1.4.0
BuildRequires: hyperledger-fabric-devel >= %{module_httpserver_version}
Requires:      hyperledger-fabric >= %{module_httpserver_version}
BuildRequires: hyperledger-fabric-ca-devel >= %{module_httpserver_version}
Requires:      hyperledger-fabric-ca >= %{module_httpserver_version}
BuildRequires: hyperledger-fabric-db-devel >= %{module_httpserver_version}
Requires:      hyperledger-fabric-db >= %{module_httpserver_version}
%endif

%if %{with southside_leveldb}
%define module_leveldb_version 2:0.2.1
BuildRequires: module-leveldb-devel >= %{module_leveldb_version}
Requires:      module-leveldb >= %{module_leveldb_version}
%endif

%if %{with southside_mysql}
%define module_mysql_version 0.3.0
BuildRequires: module-mysql-devel >= %{module_mysql_version}
Requires:      module-mysql >= %{module_mysql_version}
%endif

%if %{with southside_pgsql}
%define module_pgsql_version 0.0
BuildRequires: module-pgsql-devel >= %{module_pgsql_version}
Requires:      module-pgsql >= %{module_pgsql_version}
%endif

%if %{with southside_ramcloud}
%define module_ramcloud_version 0.0
BuildRequires: module-ramcloud-devel >= %{module_ramcloud_version}
Requires:      module-ramcloud >= %{module_ramcloud_version}
%endif

%if %{with southside_sqlite}
%define module_sqlite_version 0.13.0
BuildRequires: module-sqlite-devel >= %{module_sqlite_version}
Requires:      module-sqlite >= %{module_sqlite_version}
%endif

%if %{with southside_scarpet}
%define tunitas_scarpet_version 0.0.0
BuildRequires: tunitas-scarpet-devel >= %{tunitas_scarpet_version}
Requires:      tunitas-scarpet >= %{tunitas_scarpet_version}
%endif

%define module_boost_version 0.3.8
BuildRequires: module-boost-devel >= %{module_boost_version}
Requires:      module-boost >= %{module_boost_version}

%define module_c_version 2:0.4.0
BuildRequires: module-c-devel >= %{module_c_version}
Requires:      module-c >= %{module_c_version}

%define module_format_version 2:0.16.0
BuildRequires: module-format-devel >= %{module_format_version}
Requires:      module-format >= %{module_format_version}

%define module_half_version 0.1.1
BuildRequires: module-half-devel >= %{module_half_version}
Requires:      module-half >= %{module_half_version}

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

%define module_options_version 0.14.0
BuildRequires: module-options-devel >= %{module_options_version}
Requires:      module-options >= %{module_options_version}

%define module_posix_version 2:0.27.0
BuildRequires: module-posix-devel >= %{module_posix_version}
Requires:      module-posix >= %{module_posix_version}

# requires currency beyond 04.green-copper-heron
%define module_rabinpoly_version 2:0.2.0
BuildRequires: module-rabinpoly-devel >= %{module_rabinpoly_version}
Requires:      module-rabinpoly >= %{module_rabinpoly_version}

%define module_file_slurp_version 0.7.9
%define module_slurp_version      2:0.11.0
BuildRequires: (module-slurp-devel >= %{module_slurp_version} or module-file-surp-devel >= %{module_slurp_version})
Requires:      (module-slurp >= %{module_slurp_version} or module-file-slurp >= %{module_file_slurp_version})

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

%define module_uuid_version 0.2.3
BuildRequires: module-uuid-devel >= %{module_uuid_version}
Requires:      module-uuid >= %{module_uuid_version}

%if %{with make_check}
%define module_rigging_unit_version 0.8.1
%define module_rigging_version      2:0.10.0
BuildRequires: (module-unit-rigging-devel >= %{module_rigging_unit_version} or module-rigging-devel >= %{module_rigging_version})
%endif

%description
Runtime libraries, files and other components of Tunitas Apanolio, a "Northside" API to IAB PrivacyChain

%package devel
Summary: The development components of the Tunitas Tarwater Identity Management System
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-c++
Requires: tunitas-basics-devel
Requires: tunitas-butano-devel
%if %{with hyperledger_fabric}
Requires: hyperledger-fabric-devel
Requires: hyperledger-fabric-ca-devel
Requires: hyperledger-fabric-db-devel
%endif
%if %{with leveldb}
Requires: module-leveldb-devel
%endif
%if %{with mysql}
Requires: module-mysql-devel
%endif
%if %{with pgsql}
Requires: module-pgsql-devel
%endif
%if %{with tunitas_scarpet}
Requires: tunitas-scarpet-devel
%endif
%if %{with ramcloud}
Requires: module-ramcloud-devel
%endif
Requires: module-boost-devel
Requires: module-c-devel
Requires: module-format-devel
Requires: module-half-devel
Requires: module-json-devel
Requires: module-nonstd-devel
Requires: module-options-devel
Requires: module-posix-devel
Requires: module-rabinpoly-devel
Requires: (module-slurp-devel or module-file-surp-devel)
Requires: module-std-devel
Requires: (module-c-string-devel >= %{module_string_version} or module-string-devel >= %{module_string_version})
Requires: module-sys-devel
Requires: module-uuid-devel

%description devel
The S.C.O.L.D.-style modules of 'namespace tunitas::montara' are supplied.
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
    --with-temerarious-flagship=%{std_tunitas_prefix} --with-FIXTHIS=this_should_not_be_needed_the_std_tunitas_should_be_sufficient \
    %{?with_southside_fabric:--with-southside-fabric} \
    %{?with_southside_leveldb:--with-southside-leveldb} \
    %{?with_southside_mysql:--with-southside-mysql} \
    %{?with_southside_pgsql:--with-southside-pgsql} \
    %{?with_southside_ramcloud:--with-southside-ramcloud} \
    %{?with_southside_sqlite:--with-southside-sqlite} \
    %{?with_southside_scarpet:--with-southside-scarpet} \
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
# NO DSO, only convenience libraries ---> %%{_libdir}/*.so.*
%{systemd_systemdir}/montara.service

%files devel
%doc README.md
%{modulesdir}/*
%{_libdir}/*
# NO DSO, only convenience libraries ---> %%exclude %%{_libdir}/*.so.*
%exclude %{modulesdir}/want
%exclude %{modulesdir}/fpp/want
%exclude %{modulesdir}/hpp/want
%exclude %{modulesdir}/ipp/want

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Thu Aug 15 2019 - Wendell Baker <wbaker@verizonmedia.com> - 0.1.2-2
- preen & clean; correct installation rules during the build

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 0.1.1-2
- cram down the version number, this is still has "oh point" level of capability
- second packaging, corrected the 'make check' rules Release 02 (Towering Redwood)
- %% the macros used within the commentariat
- %%if...%%endif syntax
- rich Requires syntax
- MUST configure --with-temerarious-flagship so decorate with --with-FIXTHIS
- and require for testing module-rigging-devel >= 2:0.10.0
- do not declare ownership of the %%{modulesdir}/want directories

* Wed Jun 26 2019 - Wendell Baker <wbaker@verizonmedia.com> - 0.1.0-1
- first packaging, first release
