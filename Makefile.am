# This is a GNU -*- Makefile -*- fragment that is included by Automake
# Copyright Yahoo Inc, 2022.
# Licensed under the terms of the Apache-2.0 license.
# For terms and provenance see the LICENSE file at the top of this repository.
# For terms, see the LICENSE file at https://github.com/yahoo/tunitas-keyston/blob/master/LICENSE
# For terms, see the LICENSE file at https://git.tunitas.technology/all/components/keyston/tree/LICENSE
#
# [[FIXTHIS]] - ACLOCAL_AMFLAGS is evaluted by automake *before* make even runs
# It uses /bin/bash eval to evaluate the line ...
#    so make variables $(...) look like backticks
#    but make variables ${...} look like shell variables with defaults
#
# is a subshell
#    /usr/bin/libtoolize: line 3772: temerarious_flagship_datadir: command not found
#
# these must all be on a single line, no backslash continuations
#ACLOCAL_AMFLAGS = -I m4 -I ${temerarious_flagship_datadir:-/opt/tunitas/share/temerarious-flagship}/ac -I ${hypogeal_twilight_datadir:-/opt/scold/share/hypogeal-twilight}/m4
ACLOCAL_AMFLAGS = -I m4
AUTOMAKE_OPTIONS = no-define subdir-objects foreign
AM_MAKEFLAGS= \
  DO_NOT_REPASS_MAKEFLAGS='$(MAKEFLAGS)' \
  CPPFLAGS='$(CPPFLAGS)' \
  CXXFLAGS='$(CXXFLAGS)' \
  LDFLAGS='$(LDFLAGS)' \
  $(end)

bin_PROGRAMS = \
  $(end)
# WATCHOUT - these installable libraries MUST be in this order to congeal the rpath dependencies upon installation
lib_LTLIBRARIES = \
  lib/libtunitas-keyston.la \
  $(end)
noinst_LTLIBRARIES = \
  noinst/lib/libwant.la \
  noinst/lib/libapp.la \
  noinst/lib/libtunitas-keyston.la \
  noinst/lib/libautotools-autoconf+tunitas-keyston.la \
  noinst/lib/libfmt+tunitas-keyston.la \
  noinst/lib/libstd+tunitas-keyston.la \
  noinst/lib/libnonstd+tunitas-keyston.la \
  $(end)
check_PROGRAMS = \
  check/bin/unit \
  $(end)
check_LTLIBRARIES = \
  check/lib/libtests.la \
  $(end)

default:
# This bad design ... with limited tooling ... trying to get 'make' and one Makefile to do too many things "automatically"
# This recursion and the ordering can't be fixed or overridden.
#
# WATCHOUT ---> The default 'all' rule DOES NOT pass command-line variable embellishments down one gratuitous level
# WATCHOUT ---> all: config.h
# WATCHOUT --->	     $(MAKE) $(AM_MAKEFLAGS) all-am
# WATCHOUT --->	     $(MAKE) $(AM_MAKEFLAGS) all-am
# WATCHOUT ---> all-am: Makefile $(PROGRAMS) $(LTLIBRARIES) config.h
# WATCHOUT ---> 
# WATCHOUT ---> The default 'check' rule DOES NOT pass command-line variable embellishments down one gratuitous level
# WATCHOUT ---> check: check-am
# WATCHOUT ---> check-am: all-am
# WATCHOUT ---> 	$(MAKE) $(AM_MAKEFLAGS) $(check_PROGRAMS) $(check_LTLIBRARIES)
# WATCHOUT ---> 	$(MAKE) $(AM_MAKEFLAGS) check-TESTS
#
include tests/Makefrag.am
include @temerarious_flagship_datadir@/am/build.am

# also configure.ac and HGTW_SUBMODULE_CONFIGURE
# SUBDIRS = @subdirs@

# These match with HGTW_WITH_MODULE in configure.ac
DEVELOPMENT_AREAS = \
  $(module_cli_core_prefix) \
  $(module_fmt_prefix) \
  $(module_langu_prefix) \
  $(module_nonstd_prefix) \
  $(module_sys_prefix) \
  $(tunitas_basics_prefix) \
  $(deprecated_DEVELOPMENT_AREAS) \
  $(end)
TESTING_AREAS = \
  $(module_rigging_core_prefix) \
  $(deprecated_TESTING_AREAS) \
  $(end)
INSTALLATION_AREAS = \
  $(nonstd_fmt_prefix) \
  $(nonstd_gcc_prefix) \
  $(std_scold_prefix) \
  $(std_tunitas_prefix) \
  $(deprecated_INSTALLATION_AREAS) \
  $(end)

default: all

.PHONY: clean-local mostlyclean-local distclean-local
clean-local mostlyclean-local distclean-local::
clean-dependencies::
clean-local:: clean-dependencies

include noinst/lib/libapp.am
include check/bin/unit.am
include check/lib/libtests.am
include noinst/lib/libwant.am
include noinst/lib/libtunitas-keyston.am
include noinst/lib/libautotools-autoconf+tunitas-keyston.am
include noinst/lib/libfmt+tunitas-keyston.am
include noinst/lib/libstd+tunitas-keyston.am
include noinst/lib/libnonstd+tunitas-keyston.am
include lib/libtunitas-keyston.am

include modules/Makefrag.am # this MUST be after the relevant nonstd_lib_lib${something}_la_MODULES_ variables are defined

# --- Mostly boilerplate beyond here
#
# -Wall      ... the language isn't complete without it
# -std=c++1y ... as close to C++14 and beyond as we can get
# -std=c++1z ... as close to C++17 and beyond as we can get
# -std=c++2a ... as close to C++20 and beyond as we can get
# -std=c++2b ... as close to C++23 and beyond as we can get
# -std=c++2c ... as close to C++26 and beyond as we can get
# -ggdb      ... and recall that -ggdb and -O2 don't play well together

Makefile_COMPILER_CPPFLAGS_SET =       @CPPFLAGS_gcc@ @CPPFLAGS_gdb@
Makefile_COMPILER_CFLAGS_SET   = -Wall   @CFLAGS_gcc@   @CFLAGS_gdb@
Makefile_COMPILER_CXXFLAGS_SET = -Wall @CXXFLAGS_gcc@ @CXXFLAGS_gdb@
Makefile_COMPILER_LDFLAGS_SET  = -Wall  @LDFLAGS_gcc@  @LDFLAGS_gdb@

Makefile_nonstd_PACKAGE_CPPFLAGS_SET = @nonstd_fmt_CPPFLAGS@
Makefile_nonstd_PACKAGE_CFLAGS_SET   = @nonstd_fmt_CFLAGS@
Makefile_nonstd_PACKAGE_CXXFLAGS_SET = @nonstd_fmt_CXXFLAGS@
Makefile_nonstd_PACKAGE_LDFLAGS_SET  = @nonstd_fmt_LDFLAGS@

Makefile_PACKAGE_CPPFLAGS_SET = 
Makefile_PACKAGE_CFLAGS_SET   = 
Makefile_PACKAGE_CXXFLAGS_SET = 
Makefile_PACKAGE_LDFLAGS_SET  = 

Makefile_nonstd_CHECK_CPPFLAGS_SET = 
Makefile_nonstd_CHECK_CFLAGS_SET   = 
Makefile_nonstd_CHECK_CXXFLAGS_SET = 
Makefile_nonstd_CHECK_LDFLAGS_SET  = 

#                                                  if    did not substitute away                      then use this
#                                                  |           |                                      |            else use the substitution
#                                                  |           |              @CPPFLAGS_no_install@   |            |
#                                                  |           |              |                       |            |
#                                                  |           |              |                       |            |
#                                                  v           v              v                       v            v
Makefile_CHECK_CPPFLAGS_SET = @CPPFLAGS_cppunit@ $(if $(filter %_no_install@, @CPPFLAGS_no_install@), $(empty),    @CPPFLAGS_no_install@)
Makefile_CHECK_CFLAGS_SET   =   @CFLAGS_cppunit@ $(if $(filter %_no_install@, @CFLAGS_no_install@),   $(empty),    @CFLAGS_no_install@)
Makefile_CHECK_CXXFLAGS_SET = @CXXFLAGS_cppunit@ $(if $(filter %_no_install@, @CXXFLAGS_no_install@), $(empty),    @CXXFLAGS_no_install@)
Makefile_CHECK_LDFLAGS_SET  =  @LDFLAGS_cppunit@ $(if $(filter %_no_install@, @LDFLAGS_no_install@),  -no-install, @LDFLAGS_no_install@)

# these are assembled by .../toolflags.mk within temerarious-flagship (hypogeal-twilight) .../toolflags.mk
AM_CPPFLAGS = $(PACKAGE_CPPFLAGS_SET)
AM_CFLAGS   = $(PACKAGE_CFLAGS_SET)
AM_CXXFLAGS = $(PACKAGE_CXXFLAGS_SET)
AM_LDFLAGS  = $(V_LDFLAGS_avoid.VERBOSE_Veq$(V))
AM_LIBTOOLFLAGS = $(V_LIBTOOLFLAGS_VERBOSE_Veq$(V))

deprecated_DEVELOPMENT_AREAS = \
  $(module_cli_prefix) \
  $(module_options_prefix) \
  $(module_posix_prefix) \
  $(module_std_prefix) \
  $(module_string_prefix) \
  $(module_uuid_prefix) \
  $(end)
deprecated_TESTING_AREAS = \
  $(module_cppunit_prefix) \
  $(module_rigging_prefix) \
  $(end)
deprecated_INSTALLATION_AREAS = \
  $(nonstd_cppunit_prefix) \
  $(nonstd_libhttpserver_prefix) \
  $(end)
