# This is a GNU -*- Makefile -*- and you will need at least GNU make-4, and maybe make-4.2.1
# Copyright 2018-2019, Oath Inc.
# Licensed under the terms of the Apache-2.0 license.
# See the LICENSE file in https://github.com/yahoo/tunitas-packaging/blob/master/LICENSE for terms.

default:
PACKAGES = \
  temerarious-flagship \
  tunitas-basics \
  tunitas-tarwater \
  tunitas-rockaway \
  tunitas-pescadero \
  tunitas-grabtown \
  tunitas-lobitos \
  $(end)
PACKAGES.notready = \
  tunitas-butano \
  tunitas-montara \
  tunitas-prurissima \
  $(end)

topdir = /build/rpms
srpmdir = $(topdir)/SRPMS
rpmdir = $(topdir)/RPMS
specdir = $(topdir)/SPECS
sourcedir = $(topdir)/SOURCES

cwd := $(shell pwd)# because PWD is wrong in 'make -C <directory>'
cwd/.. = $(patsubst %/,%,$(dir $(cwd)))
cwd/../.. = $(patsubst %/,%,$(dir $(patsubst %/,%,$(dir $(cwd)))))
nearby = $(cwd/..)/sources

rpmspec-query = rpmspec --srpm -q --qf="%{name} %{version} %{release} %{arch}" $1.spec
define RECIPE1 =
$1.spec := $(shell $(call rpmspec-query, $1))
endef
define RECIPE2 =
$1.spec := $(shell $(call rpmspec-query, $1))
$(if $(filter 4,$(words $($1.spec))),$(__ok),$(error $1.spec is has $(words $($1.spec)) elements, but must have 4))
$1.name = $(word 1, $($1.spec))
$1.version = $(word 2, $($1.spec))
$1.release = $(word 3, $($1.spec))
$1.arch = $(word 4, $($1.spec))
$1.nv = $$($1.name)-$$($1.version)
$1.nvr = $$($1.name)-$$($1.version)-$$($1.release)
$1.nvr.arch = $($1.nvr.arch).$($1.arch)
$1.nv.tarz = $$($1.nv).tar.gz
$1.nvr.tarz = $$(error NO SUCH variable $1.nvr.tarz, instead use $1.nv.tarz)
$1.nv.spec = $$($1.nv).spec
$1.nvr.spec = $$(error NO SUCH variable $1.nvr.spec, instead use $1.nv.spec)
$1.nvr.src.rpm = $$($1.nvr).src.rpm
$1.nvr.arch.rpm = $$($1.nvr).$$($1.arch).rpm
endef
DIRECTORY.temerarious-flagship = $(nearby)/temerarious-flagship
DIRECTORY.tunitas-basics = $(nearby)/basics
DIRECTORY.tunitas-butano = $(nearby)/butano
DIRECTORY.tunitas-grabtown = $(nearby)/grabtown
DIRECTORY.tunitas-lobitos = $(nearby)/lobitos
DIRECTORY.tunitas-montara = $(nearby)/montara
DIRECTORY.tunitas-pescadero = $(nearby)/pescadero
DIRECTORY.tunitas-purissima = $(nearby)/purissima
DIRECTORY.tunitas-rockaway = $(nearby)/rockaway
DIRECTORY.tunitas-tarwater = $(nearby)/tarwater
define RECIPE3 =
$(rpmdir)/$$($1.nvr.arch)/$$($1.nvr.arch.rpm) : $(specdir)/$$($1.nv.spec) $(sourcedir)/$$($1.nv.tarz)
	rpmbuild -ba $(__RPMBUILD_OPTIONS) $$(word 1,$$^)
$(specdir)/$$($1.nv.spec) : $1.spec
	install -c -m 444 $$< $$@
$(sourcedir)/$$($1.nv.tarz) : PACKAGE=$$($1.nv)
$(sourcedir)/$$($1.nv.tarz) : DIRECTORY=$$(if $$(DIRECTORY.$1),$$(DIRECTORY.$1),$$(error $$(DIRECTORY.$1) is unset))
$(sourcedir)/$$($1.nv.tarz) : .ALWAYS
	tar \
	    --transform='s,^\.,$$(if $$(PACKAGE),$$(PACKAGE),$$(error PACKAGE is unset))/,' \
	    -C $$(if $$(DIRECTORY),$$(DIRECTORY),$$(error DIRECTORY is unset)) \
	    -zcf $$@ .
endef
define RECIPE4 =
.PHONY: $(addprefix package-, $1 $(patsubst tunitas-%,%,$1))
$(addprefix package-, $1 $(patsubst tunitas-%,%,$1)): $(rpmdir)/$($1.nvr.arch)/$($1.nvr.arch.rpm)
endef

SRPMS = $(addprefix $(srpmdir)/, $(foreach package,$(PACKAGES),$($(package).nvr.src.rpm)))
RPMS  = $(addprefix $(rpmdir)/, $(foreach package,$(PACKAGES),$($(package).nvr.arch)/$($(package).nvr.arch.rpm)))
SPECS = $(addprefix $(specdir)/, $(foreach package,$(PACKAGES),$($(package).nv.spec)))
TARZ  = $(addprefix $(sourcedir)/, $(foreach package,$(PACKAGES),$($(package).nv.tarz)))

# Whereas RPMBUILD_OPTIONS is reserved to the command line
Makefile_RPMBUILD_OPTIONS = --define='%_topdir $(topdir)'
__RPMBUILD_OPTIONS = $(Makefile_RPMBUILD_OPTIONS) $(RPMBUILD_OPTIONS)

clean: clean-SPECS clean-TARZ
clean-SPECS: ; rm -f $(SPECS)
clean-TARZ: ; rm -f $(TARZ)

distclean: distclean-SRPMS distclean-RPMS
distclean-RPMS: ; rm -f $(RPMS)
distclean-SRPMS: ; rm -f $(SRPMS)

$(foreach package,$(PACKAGES), \
$(eval $(call RECIPE1,$(package)))\
$(eval $(call RECIPE2,$(package)))\
$(eval $(call RECIPE3,$(package)))\
$(eval $(call RECIPE4,$(package))))

.ALWAYS: ;
clean:
all: $(RPMS)
default: all
