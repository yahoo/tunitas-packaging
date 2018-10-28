%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%define pkglibexecdir  %{_prefix}/libexec/%{name}
%define pkgdatarootdir %{_prefix}/share/%{name}
%define pkgdatadir     %{pkgdatarootdir}

Version: 1.1.3
Release: 2
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
./buildconf
./configure --prefix=%{_prefix}
%make_build

%check
%make_build check

%install
%make_install

%files
%license LICENSE
%doc ChangeLog README.md
# NOT YET ---> %%{pkglibexecdir}
%{pkgdatadir}

%changelog
# DO NOT use ISO-8601 dates; only use date +'%a %b %d %Y'

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.1.3-2
- am/compile.am provides an tf-friendly --make-depend-script within DC_OPTIONS

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.1.2-1
- INSTALLED_module_INTERFACES corrected
- include .../mk/toolflags.mk

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.1.1-1
- TF_SOURCEStoMODULENAMES accepts *.cpp and *.xcpp

* Sun Oct 28 2018 - Wendell Baker <wbaker@oath.com> - 1.1.0-4
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.

* Sat Oct 27 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-1
- first packaging, first release.
