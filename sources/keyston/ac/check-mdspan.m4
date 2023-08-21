dnl For terms and provenance see the LICENSE file at the top of this repository.
dnl
dnl WATCHOUT - (aspirationally) - this is superceded in hypogeal-twilight >= 0.53
dnl
dnl TF_CHECK_MDSPAN      (and no arguments)
dnl

dnl ----------------------------------------------------------------------------------------------------

dnl TF_CHECK_MDSPAN      (and no arguments)
dnl
dnl Validates that mdspan (built from source, there appears to be no rpm)
dnl
dnl Postcondition: (the following are set)
dnl
dnl     CPPFLAGS_mdspan
dnl     CFLAGS_mdspan
dnl     CXXFLAGS_mdspan
dnl     LDFLAGS_mdspan
dnl
dnl WATCHOUT - the expected implementation is https://github.com/kokkos/mdspan
dnl WATCHOUT - which has some very very nonstandard #define hacking within it
dnl
dnl Witness:
dnl
dnl   #ifndef MDSPAN_IMPL_STANDARD_NAMESPACE
dnl     #define MDSPAN_IMPL_STANDARD_NAMESPACE Kokkos
dnl   #endif
dnl
dnl   #ifndef MDSPAN_IMPL_PROPOSED_NAMESPACE
dnl     #define MDSPAN_IMPL_PROPOSED_NAMESPACE Experimental
dnl   #endif
dnl
AC_DEFUN([TF_CHECK_MDSPAN], [
    AC_REQUIRE([HT_ENABLE_CONFIGURE_VERBOSE])
    AC_REQUIRE([TF_WITH_NONSTD_MDSPAN])
    __CPPFLAGS_mdspan_IDIOSYNCRATIC_NAMESPACE_HACKING_DEFINITIONS="-DMDSPAN_IMPL_STANDARD_NAMESPACE=std -DMDSPAN_IMPL_PROPOSED_NAMESPACE=experimental"
    dnl the prefix is expected from an earlier invocation of HT_WITH_NOSTD_MDSPAN
    if test xNONE = "x$nonstd_mdspan_prefix" || test x = "x$nonstd_mdspan_prefix"; then
        AC_MSG_ERROR([you MUST define --nonstd-mdspan=PREFIX because there is no standard rpm installation])
        # obviously this (below) will not work until there exists a mdspan-devel in the (Fedora / Red Hat) RPM universe
        {
            #
            # Must be the system-installed one
            #
            if ! rpm -q mdspan-devel 2>/dev/null ; then
                AC_MSG_ERROR([mdspan-devel is required])
            fi
            mdspan_VERSION=$(rpm -q mdspan-devel)
            #
            # FIXTHIS - there appears to be no mdspan in the rpm distributions at all
            # You'll have to build from source
            #
            TF_CHECK_MDSPAN__PKG_CONFIG_INSTALLED_MDSPAN([])
        }
    else
        nonstd_mdspan_includedir=${nonstd_mdspan_prefix?}/include
        {
            #
            # e.g.
            # --with-nonstd-mdspan=/opt/nonstd/mdspan
            #
            # speculatively guess, then check that those directories actually exist
            for l in lib64 lib ; do
                nonstd_mdspan_libdir="${nonstd_mdspan_prefix?}/$l"
                if test -d $nonstd_mdspan_libdir ; then
                    __pkgconfigdir="${nonstd_mdspan_libdir}/pkgconfig"
                    SCOLD_MSG_VERBOSE([using the mdspan libraries in ${nonstd_mdspan_libdir?} via ${__pkgconfigdir?}])
                    TF_CHECK_MDSPAN__PKG_CONFIG_INSTALLED_MDSPAN([PKG_CONFIG_PATH=${__pkgconfigdir?}])
                    break
                fi
            done
            # check the libdir that we speculatively assigned, above
            for dir in "$nonstd_mdspan_prefix" "$nonstd_mdspan_libdir" ; do
                if  test ! -d "$dir" ; then
                    AC_MSG_ERROR([missing directory $dir is required for mdspan])
                fi
            done
        }
        # you need to have established nonstd-mdspan
        CPPFLAGS_mdspan="-I${nonstd_mdspan_includedir?} ${__CPPFLAGS_mdspan_IDIOSYNCRATIC_NAMESPACE_HACKING_DEFINITIONS}"
        CFLAGS_mdspan=
        CXXFLAGS_mdspan=
        LDFLAGS_mdspan=-L${nonstd_mdspan_libdir?} # mdspan is "header only" so this is specious
    fi
    AC_SUBST(CPPFLAGS_mdspan)
    AC_SUBST(CFLAGS_mdspan) 
    AC_SUBST(CXXFLAGS_mdspan) 
    AC_SUBST(LDFLAGS_mdspan)
])

dnl
dnl TF_CHECK_MDSPAN__PKG_CONFIG_INSTALLED_MDSPAN of 1 argument, which may be empty
dnl run pkg-config to acquire the mdspan settings
dnl
dnl $1 - setting of PKG_CONFIG_PATH
dnl
dnl Examples:
dnl     $1 - []  (empty)
dnl     $1 - PKG_CONFIG_PATH=/opt/mdspan/lib64/pkgconfig
dnl
AC_DEFUN([TF_CHECK_MDSPAN__PKG_CONFIG_INSTALLED_MDSPAN], [
    if true ; then
      AC_MSG_NOTICE([skipping pkgconfig checks because mdspan does not use pkgconfig])
    else
        if ! type -p pkg-config > /dev/null 2>&1 ; then
            AC_MSG_ERROR([pkg-config is missing])
        fi
        if ! pkg-config --print-errors mdspan ; then
            AC_MSG_ERROR([pkg-config cannot find mdspan])
        fi
        function __pkg_config() {
            local flag=[$][1]; shift
            # without print-errors, only an exit code is emitted when problems occur.
            $1 pkg-config --print-errors --$flag mdspan
        }
        # WATCHOUT - pkg-config will exit nonzero but produce nothing when it encounters an error.
        # Countermeasure: do the work twice so we can examine error codes, then capture any output on the 2nd pass.
        if ! { # FIXME - get rid of the copied code herein
               __pkg_config cflags > /dev/null &&
               __pkg_config cflags-only-I > /dev/null &&
               __pkg_config cflags-only-other > /dev/null &&
               __pkg_config libs > /dev/null &&
               __pkg_config libs-only-l > /dev/null &&
               __pkg_config libs-only-other > /dev/null &&
               __pkg_config libs-only-L > /dev/null
        } then
            AC_MSG_ERROR([$1 pkg-config fails])
        fi 
        CPPFLAGS_mdspan=$(__pkg_config cflags-only-I)
        CFLAGS_mdspan=$(__pkg_config cflags-only-other)
        CXXFLAGS_mdspan="${CFLAGS_mdspan}"
        __libs_only_l=$(__pkg_config libs-only-l)
        __libs_only_other=$(__pkg_config libs-only-other)
        __libs_only_L=$(__pkg_config libs-only-L)
        # change -L/opt/nonstd/mdspan/lib64 -> (the pair) -L/opt/nonstd/mdspan/lib64 -Wl,-rpath=/opt/nonstd/mdspan/lib64
        __libs_only_L_with_rpath="$(for L in ${__libs_only_L} ; do echo "${L?} -Wl,-rpath=${L#-L}" ; done)"
        LDFLAGS_mdspan="${__libs_only_L_with_rpath} ${__libs_only_other} ${__libs_only_l}"
    fi
])
