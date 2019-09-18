# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%define pkglibexecdir  %{_prefix}/libexec/%{name}
%define pkgdatarootdir %{_prefix}/share/%{name}
%define pkgdatadir     %{pkgdatarootdir}

%global tunitas tu02
%global tunitas_dist %{?tunitas:.%{tunitas}}

Version: 1.4.3
Release: 2%{?tunitas_dist}%{?dist}
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
BuildRequires: (SCOLD-DC or anguish-answer >= 2.0 or baleful-ballad >= 0.17 or ceremonial-contortion or demonstrable-deliciousness)
BuildRequires: hypogeal-twilight >= 0.45

Requires: hypogeal-twilight >= 2:0.45.3

# https://fedoraproject.org/wiki/Packaging:Debuginfo
%global debug_package %{nil}
BuildArch: noarch
%description
This is an autoconf build system specialized to support Tunitas.
.../ac/*.m4 are autoconf macros
.../am/*.m4 are automake fragments
.../bc/template.*-buildconf are buildconf templates

%prep
%autosetup

%build
# NO SUCH ---> ./buildconf
# NO SUCH ---> ./configure --prefix=%{_prefix}
# NO SUCH ---> %%make_build
: all done

%check
# NO SUCH ---> %%make_build check
: all checked

%install
# NO SUCH ---> %make_install
#
# you have to install by hand
# install -D creates all but the penultimate component of the target path (you frequently want this)
# install -d is the same as mkdir -p wherein arguments are created as directories (you rarely want this)
#
mkdir -p %{buildroot}%{pkgdatarootdir}/{ac,am,bc}
install -m 664 ac/*.m4 %{buildroot}%{pkgdatarootdir}/ac/.
install -m 664 am/*.mk am/*.am %{buildroot}%{pkgdatarootdir}/am/.
install -m 664 bc/template.*[^~]  %{buildroot}%{pkgdatarootdir}/bc/.

%files
%license LICENSE
# Although deprecating, leave ChangeLog in here for a while, at least
# until it is fully clear tha the NEWS file subsumes all the release notes.
%doc ChangeLog NEWS README.md
# NOT YET ---> %%{pkglibexecdir}
%{pkgdatadir}

%changelog
# DO NOT use ISO-8601 dates; only use date +'%%a %%b %%d %%Y'

* Wed Sep 18 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.4.3-2
- Be specific about the SCOLD-DC that is allowed, especially anguish-answer >= 2.0 or a recent baleful-ballad

* Sun Aug 25 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.4.3-1
- correct TF_CHECK_LEVELDB; until correct
- remove the '.tu02' particle here in the specfile; .tu02 only for the Ahead Releases (e.g. those S.C.O.L.D. modules)

* Sun Aug 25 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.4.0-1
- with TF_CHECK_LEVELDB, TF_WITH_NONSTD_LEVELDB

* Fri Aug 23 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.3.4-1
- license badging in buildconf

* Fri Aug 23 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.3.3-1
- burn a new patch-level number to resynchronize the project and the package
- incorporate fix for aclocal: error: couldn't open directory '/opt/tunitas/ac': No such file or directory

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.3.1-2
- no recursion in debug

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.3.1-1
- template of .../bc/template.autotools-buildconf corrected to use the devel-or-production temerarious_flagship_datadir_ac

* Sun Aug 11 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.3.0-1
- current legal boilerplate
- supplies TF_PROG_PROTOC
- require hypogeal-twilight >= 2:0.45.3

* Mon Jul 15 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.2.0-5
- perform the packaging from branch series/v1.2/02.towering-redwood and with the consistent %%version adn %%changelog

* Mon Jul 15 2019 - Wendell Baker <wbaker@verizonmedia.com> - 1.2.0-4
- first build of Release 02 (Towering Redwood)

* Mon Oct 29 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.2.0-3
- define TF_V_DIS, TF_V_DONE, TF_V_1ST, TF_V_2ND
- override .../mk/toolflags.mk filtration computation to organize SEARCHPATH NEAR before THERE

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.1.4-1
- bc/template.autotools-buildconf corrections and exit EX_SOFTWARE

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.1.3-2
- am/compile.am provides an tf-friendly --make-depend-script within DC_OPTIONS

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.1.2-1
- INSTALLED_module_INTERFACES corrected
- include .../mk/toolflags.mk

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.1.1-1
- TF_SOURCEStoMODULENAMES accepts *.cpp and *.xcpp

* Sun Oct 28 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.1.0-4
- reminder: changes to the packaging itself are recorded herein.
  major change to the project feature-function set and invariants are
  described in the project ChangeLog and the project git log.
  consequently, minimal change notations are made herein.

* Sat Oct 27 2018 - Wendell Baker <wbaker@verizonmedia.com> - 1.0.0-1
- first packaging, first release.
