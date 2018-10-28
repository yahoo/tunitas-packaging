%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%define pkglibexecdir  %{_prefix}/libexec/%{name}
%define pkgdatarootdir %{_prefix}/share/%{name}
%define pkgdatadir     %{pkgdatarootdir}

Version: 1.0.0
Release: 1
Name: temerarious-flagship
Summary: Tunitas Build System
License: Apache-2.0

Source0: %{name}-%{version}.tar.gz

BuildRequires: automake, autoconf, libtool, make
# You will be using C++.  Clang?  Someday.
BuildRequires: gcc-c++ >= 7.1.0
# But until ModulesTS is available S.C.O.L.D methodology is used.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Rich.2FBoolean_dependencies
# http://rpm.org/user_doc/boolean_dependencies.html
BuildRequires: (SCOLD-DC or anguish-answer or baleful-ballad or ceremonial-contortion or demonstrable-deliciousness)

BuildArch: noarch
%description
This is an autoconf build system specialized to support Tunitas.
.../ac/*.m4 are autoconf macros
.../am/*.m4 are automake fragments
.../bc/template.*-buildconf are buildconf templates

%prep
%autosetup

%build
: nothing to build {yet}

%check
: nothing to check {yet}

%install
: install manually
mkdir -p %{buildroot}%{pkgdatadir}/{ac,am,bc}
install -c -m 444 ac/*.m4 %{buildroot}%{pkgdatadir}/ac/.
install -c -m 444 am/*.mk %{buildroot}%{pkgdatadir}/am/.
install -c -m 444 bc/template.*-buildconf %{buildroot}%{pkgdatadir}/bc/.

%files
%license LICENSE
%doc ChangeLog README.md
# NOT YET ---> %%{pkglibexecdir}
%{pkgdatadir}

%changelog
# DO NOT use ISO-8601 dates; only use date +'%a %b %d %Y'

* Sat Oct 27 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-1
- first packaging, first release



