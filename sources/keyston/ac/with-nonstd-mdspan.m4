dnl Of course this is -*- m4 -*- to be processed by aclocal and autoconf
dnl For terms and provenance see the LICENSE file at the top of this repository.
dnl
dnl WATCHOUT - (aspirationally) - this is superceded in hypogeal-twilight >= 0.53
dnl
dnl TF_WITH_NONSTD_MDSPAN    (no arguments)
dnl 
dnl Side-Effects:
dnl
dnl   nonstd_mdspan_prefix
dnl   nonstd_mdspan_bindir
dnl   nonstd_mdspan_includedir
dnl   nonstd_mdspan_libdir
dnl   nonstd_mdspan_CPPFLAGS
dnl   nonstd_mdspan_CFLAGS
dnl   nonstd_mdspan_CXXFLAGS
dnl   nonstd_mdspan_LDFLAGS
dnl   nonstd_mdspan_PKG_CONFIG_PATH
dnl

dnl ----------------------------------------------------------------------------------------------------

AC_DEFUN([TF_WITH_NONSTD_MDSPAN], [
    AC_REQUIRE([HT_ENABLE_CONFIGURE_VERBOSE])
    TFprivate_WITH_NONSTD_MDSPAN__UNGUARDED([nonstd-mdspan], [nonstd_mdspan], [Non-standard DBus C++], [nonstd_mdspan])
])

dnl
dnl TFprivate_WITH_NONSTD_MDSPAN_UNGUARDED_GUARDED($1, $2, $3, $4)
dnl
dnl    $1 - argument name-with-dashes          e.g. nonstd-name-pattern
dnl    $2 - argument name_with_underscores     e.g. nonstd-name_pattern
dnl    $3 - explanation fragment               e.g. Non-Standard NAME stuff
dnl    $4 - the autoconf name for $1, they map illegal characters to _ (underscore)
dnl         we will map what autoconf finds at $4 to $2, a name we like better
dnl
dnl Follows the private (TFprivate) recipe laid out in hypgeal-twilight ac/with-nonstd.m4
dnl Does not reproduce all the guarding for the empty arguments.  Don't provide empty arguments.  Just don't do it.
dnl
AC_DEFUN([TFprivate_WITH_NONSTD_MDSPAN__UNGUARDED], [
    AC_REQUIRE([HT_ENABLE_CONFIGURE_VERBOSE])
    AC_ARG_WITH([$1],
                [AS_HELP_STRING([--without-$1], [without the $1 subsystem])])
    AC_MSG_CHECKING([non-standard subsystem $1])
    if test "x$with_$4" = "xno" ||
       test "x$with_$4" = "xNONE" ||
       test "x$with_$4" = "x"
    then
        AC_MSG_RESULT([no])
        unset $2_prefix
    elif test "x$with_$4" = "xyes"
    then
        AC_MSG_RESULT([FAIL])
        AC_MSG_ERROR([--with-$1=ROOT must specify a path but --with-$1=${with_$4?} appears])
    else
        AC_MSG_RESULT([${with_$4?}])
        $2_prefix=${with_$4?}
    fi
    HT_MSG_VERBOSE([acting as if presented with --with-$1=${with_$4:-no}, making that choice explicit for possible recursion])
    HT_APPEND_SUBCONFIGURE_ARGUMENT([--with-$1], [${$2_prefix:-no}])
    if test x != x${$2_prefix}
    then
        TFprivate_WITH_NONSTD_MDSPAN___PREFIX_IS_SET_CHECK_AND_ACT([$1], [$2], [$3], [$4])
    fi
    with_module_accretion_list="$with_module_accretion_list $1" # for use in [HT]_[FINALIZE]
    AC_SUBST($2_prefix)
    AC_SUBST($2_bindir)
    AC_SUBST($2_includedir)
    AC_SUBST($2_libdir)
    AC_SUBST($2_CPPFLAGS)
    AC_SUBST($2_CFLAGS)
    AC_SUBST($2_CXXFLAGS)
    AC_SUBST($2_LDFLAGS)
    AC_SUBST($2_PKG_CONFIG_PATH)
])

dnl
dnl TFprivate_WITH_PREFIX_IS_SET_CHECK_AND_ACT($1, $2, $3, $4)
dnl
dnl    $1 - argument name-with-dashes          e.g. nonstd-name-pattern
dnl    $2 - argument name_with_underscores     e.g. nonstd-name_pattern
dnl    $3 - explanation fragment               e.g. Non-Standard NAME stuff
dnl    $4 - the autoconf name for $1, they map illegal characters to _ (underscore)
dnl         we will map what autoconf finds at $4 to $2, a name we like better
dnl
dnl Postconditions:
dnl
dnl   Sets the following variables
dnl
dnl     $2_CPPFLAGS
dnl     $2_CFLAGS
dnl     $2_CXXFLAGS
dnl     $2_LDFLAGS
dnl
dnl Same arguments as
dnl
dnl   TFprivate_WITH_NONSTD_MDSPAN_UNGUARDED($1, $2, $3, $4)
dnl
dnl Copy-Pasta from hypogeal-twilight ac/with-nonstd 
dnl
AC_DEFUN([TFprivate_WITH_NONSTD_MDSPAN___PREFIX_IS_SET_CHECK_AND_ACT], [
    #
    # Whereas $2_prefix is set, we must check it and act upon it.
    #
    if ! test -d ${$2_prefix?}
    then
        AC_MSG_ERROR([no directory ${$2_prefix} exists for --with-$1=${$2_prefix?}])
    fi
    {
        $2_bindir=${$2_prefix?}/bin
        if test ! -d ${$2_bindir?}
        then
            # just a notice, not a warning
            AC_MSG_WARN([the directory ${$2_bindir?} is missing])
        fi
        HT_MSG_VERBOSE([using (executable) path ${$2_bindir?}])
    }; {
        $2_includedir=${$2_prefix?}/include
        if test ! -d ${$2_includedir?}
        then
            AC_MSG_WARN([the directory ${$2_includedir?} is missing])
        fi
        HT_MSG_VERBOSE([using searchpath ${$2_includedir?}])
    }; {
        $2_libdir=${$2_prefix?}/lib64
        AC_MSG_CHECKING([for a separable 64-bit library area])
        if test -d ${$2_libdir?}
        then
            AC_MSG_RESULT([yes])
        else
            AC_MSG_RESULT([no])
            $2_libdir=${$2_prefix}/lib
            if test ! -d ${$2_libdir?}
            then
                AC_MSG_WARN([the directory ${$2_libdir?} is missing])
            fi
        fi
        HT_MSG_VERBOSE([using loadpath ${$2_libdir?}])
    }; {
        $2_PKG_CONFIG_PATH=${$2_libdir?}/pkgconfig
        AC_MSG_CHECKING([for a pkgconfig area])
        if ! test -d ${$2_PKG_CONFIG_PATH?}
        then
             AC_MSG_RESULT([no])
             AC_MSG_NOTICE([the directory ${$2_PKG_CONFIG_PATH?} is missing])
             AC_MSG_NOTICE([apparently $1 does not use the pkgconfig system])
         else
             AC_MSG_RESULT([yes])
             HT_MSG_VERBOSE([the pkgconfig path will include ${$2_PKG_CONFIG_PATH?}])
             # WATCHOUT - these things can have funky names ... (with dangerous shell metachars?)
             __nonstd_pkgconfig_file="m4_bpatsubst([$1], [^nonstd-], []).pc"
             __nonstd_pkgconfig_path="${$2_libdir?}/pkgconfig/${__nonstd_pkgconfig_file?}"
             AC_MSG_CHECKING([for a pkgconfig file named ${__nonstd_pkgconfig_file?}])
             if test ! -f "${__nonstd_pkgconfig_path?}"
             then
                 AC_MSG_RESULT([no])
             else
                 AC_MSG_RESULT([yes])
                 dnl Being "with" the nonstandard subsystem does not mean that it is checked and ready.
                 dnl See the separable CHECK directives, e.g.
                 dnl SCOLD_CHECK_{ BOOST, CPPUNIT, CURL, CURLPP, JSONCPP, MYSQL (MYSQLPP), SQLITE, UUID }
                 HT_MSG_VERBOSE([not loading the pkg-config ${__nonstd_pkgconfig_file?}, just yet])
             fi
        fi
    }
    HT_MSG_VERBOSE([using loadpath ${$2_libdir?}])
    # WATCHOUT - these things can have funky names ... (with dangerous shell metachars?)
    __nonstd_pkgconfig_file="m4_bpatsubst([$1], [^nonstd-], [])"
    __nonstd_pkgconfig_path="${$2_libdir}/pkgconfig/${__nonstd_pkgconfig_file?}"
    AC_MSG_CHECKING([for a pkgconfig file named ${__nonstd_pkgconfig_file?}])
    if test ! -f "${__nonstd_pkgconfig_path?}"
    then
        AC_MSG_RESULT([no])
    else
        AC_MSG_RESULT([yes])
    fi
    nonstd_cppflags=""
    nonstd_cflags=""
    nonstd_cxxflags=""
    nonstd_ldflags=""
    case $1 in
    ( nonstd-gcc )
        dnl We "enable" the features of gcc separately.
        dnl The flags and searchpath for gcc are SCOLD_ENABLE_GCC, nearby
        dnl NOT HERE ---> nonstd_cxxflags="-std=c++1z -fconcepts"
        ;;
    ( * )
        dnl Being "with" the nonstandard subsystem does not mean that it is checked and ready.
        dnl See the separable CHECK directives, e.g.
        dnl SCOLD_CHECK_{ BOOST, CPPUNIT, CURL, CURLPP, JSONCPP, MYSQL (MYSQLPP), SQLITE, UUID }
        HT_MSG_VERBOSE([not loading the pkg-config ${__nonstd_pkgconfig_file?}, just yet])
        ;;
    esac
    #
    # These variables are now available "as a resource"
    # They are not yet entrained into the compilation flow.
    #
    # See the Makefile.am stanza around PACKAGE, CHECK and AND_CHECK ${TOOL}FLAGS_SET
    # Also
    #   nonstd_${COMPONENT}_${TOOL}FLAGS     established herein
    #   ${TOOL}FLAGS_${COMPONENT}            established by SCOLD_CHECK_${COMPONENT}
    #
    $2_CPPFLAGS="-I${$2_includedir?}${nonstd_cppflags:+ ${nonstd_cppflags}}"
    $2_CFLAGS="${nonstd_cflags?}"
    $2_CXXFLAGS="${nonstd_cxxflags?}"
    # the -L and -rpath are both individually & separately required
    # also equivalent is "-Xlinker -rpath=${$2_libdir}"
    $2_LDFLAGS="-L${$2_libdir?} -Wl,-rpath -Wl,${$2_libdir?}${nonstd_ldflags:+ ${nonstd_ldflags}}"
])
