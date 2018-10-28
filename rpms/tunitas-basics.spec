%global _prefix /opt/tunitas
%define modulesdir %{_prefix}/modules

%global std_tunitas_prefix /opt/tunitas
%global std_scold_prefix   /opt/scold

Version: 1.0.0
Release: 1
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

BuildRequires: temerarious-flagship

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

%build
eval \
    prefix=%{_prefix} \
    with_temerarious_flagship=%{std_tunitas_prefix} \
    with_hypogeal_twilight=%{std_scold_prefix} \
    ./buildconf
./configure --prefix=%{_prefix}
%make_build

%check
%make_check

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
# DO NOT use ISO-8601 dates; only use date +'%a %b %d %Y'

* Sat Oct 27 2018 - Wendell Baker <wbaker@oath.com> - 1.0.0-1
- first packaging, first release



