dnl This is a GNU -*- autoconf -*- specification that is processed by Autoconf.
dnl Copyright Yahoo Inc.
dnl Licensed under the terms of the Apache-2.0 license.
dnl For terms, see the LICENSE file at https://github.com/yahoo/tunitas-keyston/blob/master/LICENSE
dnl For terms, see the LICENSE file at https://git.tunitas.technology/all/components/keyston/tree/LICENSE
dnl
dnl Build Instructions are in the nearby README.md
dnl
dnl ./maintenance/nearby is a developer-centric build recipe; it guesses about nearby source trees
dnl
dnl ./buildconf &&
dnl ./configure --prefix=/opt/tunitas &&
dnl make &&
dnl make check &&
dnl make install &&
dnl echo OK DONE
dnl
AC_INIT([keyston], [0.2.0], [tunitas@yahooinc.com])
TF_INIT(AC_PACKAGE_NAME, AC_PACKAGE_VERSION, AC_PACKAGE_BUGREPORT)
AM_SILENT_RULES([yes]) dnl See the AUTOMAKE_OPTIONS in the Makefile.am

AC_CONFIG_SRCDIR([src/tunitas/keyston/Version.xcpp])
AC_CONFIG_MACRO_DIRS([m4 ac])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile])
#
# To have submodules
#   configure.ac: HGTW_CONFIG_SUBMODULES([submodules], [...list...])
#   Makefile.am:  SUBDIRS = @subdirs@
# to have no submodules
#   comment these schemes out in both places
#

TF_COMPONENT_METADIRECTORY_TIERS
TF_ENABLE_GNU
TF_ENABLE_GDB
TF_ENABLE_GCC
TF_ENABLE_LIBTOOL_NO_INSTALL
TF_ENABLE_MOCK_BUILD

TF_WITH_STD([scold])
TF_WITH_STD([tunitas])

TF_WITH_SUBSYSTEM([temerarious-flagship], [], [The Tunitas Build System])
TF_WITH_SUBSYSTEM([tunitas-basics], [], [The Tunitas Basics])

# and mention in $(DEVELOPMENT_AREAS) in Makefile.am
TF_WITH_MODULE([boost])
TF_WITH_MODULE([crypto])
TF_WITH_MODULE([cli-core])
TF_WITH_MODULE([fmt])
TF_WITH_MODULE([langu])
TF_WITH_MODULE([nonstd])
TF_WITH_MODULE([sys])
TF_WITH_MODULE([yaml])
TF_WITH_MODULE([rigging-core])

dnl deprecating (being subsumed by the above)
TF_WITH_MODULE([posix])
TF_WITH_MODULE([std])
TF_WITH_MODULE([string]) dnl a.k.a. c-string
TF_WITH_MODULE([uuid])
TF_WITH_MODULE([cppunit])

TF_MSG_VERBOSE([compiler-specific (alphabetical)])
TF_WITH_NONSTD([boost])
TF_WITH_NONSTD([cppunit])
TF_WITH_NONSTD([fmt])
TF_WITH_NONSTD([gcc]) dnl but modern gcc-12 & beyond is fine
TF_WITH_NONSTD([yaml_cpp])

AC_PREREQ([2.71])
LT_PREREQ([2.4.7])
LT_INIT
AC_LANG([C++])
AC_PROG_CC
AC_PROG_CXX
AM_PROG_CC_C_O
TF_PROG_DC

TF_CHECK_CPPUNIT
TF_CHECK_BOOST
TF_CHECK_MDSPAN

dnl Since some parts of keyston still use tunitas::number in libtunitas-number.la which uses gmp
dnl
dnl gmp-6.2.1
dnl Specimen:
dnl
dnl   gmp-6.2.1-3.fc37.x86_64
dnl   gmp-c++-6.2.1-3.fc37.x86_64
dnl   gmp-devel-6.2.1-3.fc37.x86_64
dnl
TF_CHECK_PACKAGES_ERROR([gmpxx.h], [gmp-devel])

dnl however Most of keyston transitions to use tunitas::integer which relies on Boost.Multiprecision (and not the gmp part)
dnl
dnl boost-1.78
dnl Specimen:
dnl
dnl   boost-devel-1.78.0-9.fc37.x86_64
dnl
CPPFLAGS="${CPPFLAGS} ${module_boost_prefix:+-I${module_boost_prefix?}/modules -I${module_boost_prefix?}/include} ${nonstd_boost_prefix:+-I${nonstd_boost_prefix?}/include}" # [[FIXTHIS]] fix TF_CHECK_PACKAGES to be cognizant of the now-accreted searchpath
TF_CHECK_PACKAGES_ERROR([boost/multiprecision/cpp_int.hpp], [boost-devel])
TF_CHECK_PACKAGES_ERROR([boost.multiprecision.cpp_int], [module-boost])

dnl
dnl Whereas std::mdspan "isn't ready" yet
dnl See https://en.wikipedia.org/wiki/C++23
dnl See https://gcc.gnu.org/projects/cxx-status.html (std::mdspan is not yet listed circa 2023-07)
dnl
dnl This tests for an aftermarket std::mdspan since gcc doesn't seem to have it yet
dnl See https://github.com/kokkos/mdspan
dnl
CPPFLAGS="${CPPFLAGS} ${mdspan_prefix:+-I${mdspan_prefix?}/modules -I${mdspan_prefix?}/include} ${nonstd_mdspan_prefix:+-I${nonstd_mdspan_prefix?}/include}" # [[FIXTHIS]] fix TF_CHECK_PACKAGES to be cognizant of the now-accreted searchpath
TF_CHECK_PACKAGES_ERROR([mdspan/mdspan.hpp], [mdspan-devel], [(experimental) aftermarket mdspan of C++23])
TF_CHECK_PACKAGES_ERROR([mdspan/mdarray.hpp], [mdspan-devel], [(experimental) aftermarket mdspan of C++23])

TF_FINALIZE
