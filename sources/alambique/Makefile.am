# This is a GNU -*- Makefile -*- fragment that is included by Automake
# Copyright Yahoo Inc.
# Licensed under the terms of the Apache-2.0 license.
# For terms, see the LICENSE file at https://github.com/yahoo/tunitas-alambique/blob/master/LICENSE
# For terms, see the LICENSE file at https://git.tunitas.technology/all/services/alambique/tree/LICENSE
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
  bin/flow-alambique \
  $(end)
# WATCHOUT - these installable libraries MUST be in this order to congeal the rpath dependencies upon installation
lib_LTLIBRARIES = \
  lib/libtunitas-alambique.la \
  $(end)
noinst_LTLIBRARIES = \
  noinst/lib/libapp.la \
  noinst/lib/libapp-flow-alambique.la \
  noinst/lib/libtunitas-alambique.la \
  noinst/lib/libstd+tunitas-alambique.la \
  noinst/lib/libautotools-autoconf+tunitas-alambique.la \
  $(end)
check_PROGRAMS = \
  check/bin/unit \
  check/bin/flow-alambique \
  $(end)
check_LTLIBRARIES = \
  check/lib/libtests.la \
  $(end)

default:
# This is bad design ... with limited tooling ... trying to get 'make' and one Makefile to do too many things "automatically"
# This use of recursion and the ordering can't be fixed or overridden.
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
  $(module_boost_prefix) \
  $(module_crypto_prefix) \
  $(module_cli_core_prefix) \
  $(module_fmt_prefix) \
  $(module_langu_prefix) \
  $(module_nonstd_prefix) \
  $(module_sys_prefix) \
  $(tunitas_basics_prefix) \
  $(tunitas_keyston_prefix) \
  $(deprecated_DEVELOPMENT_AREAS) \
  $(end)
TESTING_AREAS = \
  $(module_rigging_core_prefix) \
  $(module_rigging_app_prefix) \
  $(deprecated_TESTING_AREAS) \
  $(end)
INSTALLATION_AREAS = \
  $(nonstd_cryptopp_prefix) \
  $(nonstd_fmt_prefix) \
  $(nonstd_gcc_prefix) \
  $(nonstd_mdspan_prefix) \
  $(opt_scold_prefix) \
  $(opt_tunitas_prefix) \
  $(deprecated_INSTALLATION_AREAS) \
  $(end)

default: all

.PHONY: clean-local mostlyclean-local distclean-local
clean-local mostlyclean-local distclean-local::
clean-dependencies::
clean-local:: clean-dependencies

include bin/flow-alambique.am
include noinst/lib/libapp.am
include noinst/lib/libapp-flow-alambique.am
include check/bin/unit.am
include check/bin/flow-alambique.am
include check/lib/libtests.am
include noinst/lib/libtunitas-alambique.am
include noinst/lib/libstd+tunitas-alambique.am
include noinst/lib/libautotools-autoconf+tunitas-alambique.am
include lib/libtunitas-alambique.am

include modules/Makefrag.am # this MUST be after the various $(noinst_lib_lib${something_something_dark_side}_la_MODULES) variablses are defined

# --- Mostly boilerplate beyond here
#
# -Wall      ... the language isn't complete without it
# -ggdb      ... and recall that -ggdb and -O2 don't play well together [[verify]] is that still true?
#
# -std=c++1y ... as close to C++14 and beyond as we can get
# -std=c++1z ... as close to C++17 and beyond as we can get
# -std=c++2a ... as close to C++20 and beyond as we can get
# -std=c++2b ... as close to C++23 and beyond as we can get (you are here)
# -std=c++2c ... as close to C++26 and beyond as we can get (you need to get here)

Makefile_COMPILER_CPPFLAGS_SET =       @CPPFLAGS_gcc@ @CPPFLAGS_gdb@
Makefile_COMPILER_CFLAGS_SET   = -Wall   @CFLAGS_gcc@   @CFLAGS_gdb@
Makefile_COMPILER_CXXFLAGS_SET = -Wall @CXXFLAGS_gcc@ @CXXFLAGS_gdb@
Makefile_COMPILER_LDFLAGS_SET  = -Wall  @LDFLAGS_gcc@  @LDFLAGS_gdb@

Makefile_nonstd_PACKAGE_CPPFLAGS_SET = @nonstd_boost_CPPFLAGS@ @nonstd_cryptopp_CPPFLAGS@ @nonstd_fmt_CPPFLAGS@ @nonstd_mdspan_CPPFLAGS@
Makefile_nonstd_PACKAGE_CFLAGS_SET   = @nonstd_boost_CFLAGS@   @nonstd_cryptopp_CFLAGS@   @nonstd_fmt_CFLAGS@   @nonstd_mdspan_CPPFLAGS@
Makefile_nonstd_PACKAGE_CXXFLAGS_SET = @nonstd_boost_CXXFLAGS@ @nonstd_cryptopp_CXXFLAGS@ @nonstd_fmt_CXXFLAGS@ @nonstd_mdspan_CPPFLAGS@
Makefile_nonstd_PACKAGE_LDFLAGS_SET  = @nonstd_boost_LDFLAGS@  @nonstd_cryptopp_LDFLAGS@  @nonstd_fmt_LDFLAGS@  @nonstd_mdspan_CPPFLAGS@

Makefile_PACKAGE_CPPFLAGS_SET = @CPPFLAGS_boost@ $(CPPFLAGS_fmt) @CPPFLAGS_mdspan@
Makefile_PACKAGE_CFLAGS_SET   = @CFLAGS_boost@   $(CFLAGS_fmt)   @CFLAGS_mdspan@
Makefile_PACKAGE_CXXFLAGS_SET = @CXXFLAGS_boost@ $(CXXFLAGS_fmt) @CXXFLAGS_mdspan@
Makefile_PACKAGE_LDFLAGS_SET  = @LDFLAGS_boost@  $(LDFLAGS_fmt)  @LDFLAGS_mdspan@

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
