dnl This is a GNU -*- autoconf -*- specification that is processed by Autoconf.
dnl Copyright Yahoo Inc.
dnl Licensed under the terms of the Apache-2.0 license.
dnl For terms, see the LICENSE file at https://github.com/yahoo/tunitas-alambique/blob/master/LICENSE
dnl For terms, see the LICENSE file at https://git.tunitas.technology/all/services/alambique/tree/LICENSE
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
AC_INIT([alambique], [0.0.0], [tunitas@yahooinc.com])
TF_INIT(AC_PACKAGE_NAME, AC_PACKAGE_VERSION, AC_PACKAGE_BUGREPORT)
AM_SILENT_RULES([yes]) dnl See the AUTOMAKE_OPTIONS in the Makefile.am

AC_CONFIG_SRCDIR([src/tunitas/alambique/namespace.xcpp])
AC_CONFIG_MACRO_DIR([m4])
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

TF_WITH_OPT([scold])
TF_WITH_OPT([tunitas])

TF_WITH_SUBSYSTEM([temerarious-flagship], [], [The Tunitas Build System])
TF_WITH_SUBSYSTEM([tunitas-basics], [], [The Tunitas Basics])
TF_WITH_SUBSYSTEM([tunitas-keyston], [], [The Tunitas Keyston])

# and mention in $(DEVELOPMENT_AREAS) in Makefile.am
TF_WITH_MODULE([cli-core])
TF_WITH_MODULE([fmt])
TF_WITH_MODULE([langu])
TF_WITH_MODULE([nonstd])
TF_WITH_MODULE([sys])
TF_WITH_MODULE([rigging-core])
TF_WITH_MODULE([rigging-app])

dnl deprecating (being subsumed by the above)
TF_WITH_MODULE([posix])
TF_WITH_MODULE([std])
TF_WITH_MODULE([string]) dnl a.k.a. c-string
TF_WITH_MODULE([uuid])
TF_WITH_MODULE([cppunit])

TF_MSG_VERBOSE([compiler-specific (alphabetical)])
TF_WITH_NONSTD([cppunit])
TF_WITH_NONSTD([fmt])
TF_WITH_NONSTD([gcc]) dnl but modern gcc-12 & beyond is fine

AM_PROG_AR
LT_PREREQ([2.4.2])
LT_INIT
AC_PROG_CC
AC_PROG_CXX
AM_PROG_CC_C_O
TF_PROG_DC

TF_CHECK_CPPUNIT

TF_FINALIZE
