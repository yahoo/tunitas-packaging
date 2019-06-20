# Required Packages

This document contains an estimate of the tools, components their versions which you will need to build all of the Tunitas family of projects. This packaging repository is considered the "lead" or "top repository for the Tunitas family of projects.

This file documents the major packages which are necessary to build

## Required Packages

Lists of required packages are maintained in the `dependencies` directory.

* [Fedora.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/Fedora.list) - Standard Fedora packages
* [nonstd.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/nonstd.list) - Non-Standard packaging of Standard Fedora, <em>i.e.</em> patches.
* [Tunitas.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/Tunitas.list) - Core components

## Development Tooling

This is a C++ project.  The project approaches the upcoming C++20 standard, where available.

### C++ 2a Compiler
* `gcc-c++` >= 7.2, feasible.
* `gcc-c++` >= 8.2, current.
* `gcc-c++` >= 9.0, preferred.
* gcc-c++ with [C++ Modules TS](https://gcc.gnu.org/wiki/cxx-modules).

### Build Support

* The [GNU Autotools](https://www.gnu.org/software/automake/manual/html_node/index.html#Top)
    * `automake` >= 1.16
    * `autoconf` >= 2.69
    * `libtool` >= 2.4
    * `make` >= 4.2
* The Tunitas Build System
    * [temerarious-flagship](https://github.com/yahoo/temerarious-flagship) >= 1.0.0, some build system components
* The [S.C.O.L.D.](https://www.scold-lang.org) [toolchain](https://git.scold-lang.org/core) and modules
    * [hypogeal-twilight](https://git.scold-lang.org/core/hypogeal-twilight) >= 0.43, fundamental build system components.
    * [incendiary-sophist](https://git.scold-lang.org/core/incendiary-sophist) >= 0.1, the test harness, is optional.
    * [anguish-answer](https://git.scold-lang.org/core/anguish-answer) >= 0.1, the preprocessor towards a [unitary build](https://mesonbuild.com/Unity-builds.html).
* `perl` prefer `perl` >= 5.28
    * and various perl modules, surely.

##  Components

This section enumerates is a best-estimate abstraction of the component dependencies for Tunitas in a general sense.

These packages are available via `dnf` or `yum`, if your machine is configured appropriately.

* `gcc-c++` >= 8.2.1
* `cppunit-devel` >= 1.14.0
* `jsoncpp-devel` >= 1.8.4
* `httpd-devel` >= 2.4.34, `apr-util-devel` >= 1.6.1, `libapreq2-libs` >= 2.13-31
* `librabinpoly-devel` >= 0.12.0
* `libuuid-devel` >= 2.32

Modules: [apache-httpd-api](https://git.scold-lang.org/useful/apache-httpd-api), [json](https://git.scold-lang.org/modules/json), [nonstd](https://git.scold-lang.org/modules/nonstd), [options](https://git.scold-lang.org/modules/options), [posix](https://git.scold-lang.org/modules/posix), [rabinpoly](https://git.scold-lang.org/modules/rabinpoly), [std](https://git.scold-lang.org/modules/std), [string](https://git.scold-lang.org/modules/string), [sys](https://git.scold-lang.org/modules/sys), [uuid](https://git.scold-lang.org/modules/uuid); [cppunit](https://git.scold-lang.org/modules/cppunit), [rigging](https://git.scold-lang.org/modules/rigging).

## Operating System

Development commenced on Fedora 27 and has continued across Fedora 28 and Fedora 30.

A recent Ubuntu should be fine.

## Availabilities

* [Fedora](https://getfedora.com)
    * Fedora 27, possible.
    * Fedora 28, available.
    * Fedora 29, current.
    * Fedora 30, current.
* [Tunitas](https://github.com/yahoo/tunitas-packaging/blob/master/README.md)
    * <em>Release 01 (Famous Oak)</em>, current.
    * <em>Release 02 (Towering Redwood)</em>, forthcoming, the date is TBD.
* [S.C.O.L.D. C++](https://www.scold-lang.org) (Scalable Object Location Disaggregation)
    * <em>Release 02 (Maroon Iron Crow)</em>, possible.
    * <em>Release 03 (Red Mercury Goose)</em>, current
    * <em>Release 04 (Green Copper Heron)</em>, preferred.
