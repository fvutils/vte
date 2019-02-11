
SCRIPTS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(SCRIPTS_DIR)/..)
PACKAGES_DIR ?= $(ROOT_DIR)/packages
LIB_DIR = $(ROOT_DIR)/lib
BUILD_DIR := $(ROOT_DIR)/build

BUILD_DEPS += $(BUILD_DIR)/pyyaml.d
BUILD_DEPS += $(BUILD_DIR)/jinja2.d
BUILD_DEPS += $(BUILD_DIR)/markupsafe.d
EDAPACK_BUILD_URL=https://github.com/EDAPack/edapack-build

-include $(PACKAGES_DIR)/packages.mk
include $(ROOT_DIR)/etc/ivpm.info

JINJA2_VERSION=2.10
JINJA2_DIR=Jinja2-$(JINJA2_VERSION)
JINJA2_TGZ=$(BUILD_DIR)/$(JINJA2_DIR).tar.gz
JINJA2_URL=https://github.com/pallets/jinja/releases/download/$(JINJA2_VERSION)/$(JINJA2_DIR).tar.gz

PYYAML_VERSION=3.13
PYYAML_DIR=pyyaml-$(PYYAML_VERSION)
PYYAML_TGZ=$(BUILD_DIR)/$(PYYAML_DIR).tar.gz
PYYAML_URL=https://github.com/yaml/pyyaml/archive/$(PYYAML_VERSION).tar.gz

MARKUPSAFE_VERSION=1.0
MARKUPSAFE_DIR=markupsafe-$(MARKUPSAFE_VERSION)
MARKUPSAFE_TGZ=$(BUILD_DIR)/$(MARKUPSAFE_DIR).tar.gz
MARKUPSAFE_URL=https://github.com/pallets/markupsafe/archive/$(MARKUPSAFE_VERSION).tar.gz

PACKAGE=$(BUILD_DIR)/vte-$(version).tar.gz

RULES := 1

ifeq (true,$(PHASE2))
build : $(BUILD_DEPS)
else
build : $($(name)_deps)
	$(Q)$(MAKE) -f $(SCRIPTS_DIR)/ivpm.mk PHASE2=true VERBOSE=$(VERBOSE) build
endif

ifeq (true,$(PHASE2))
clean :
else
clean : $($(name)_clean_deps)
	$(Q)$(MAKE) -f $(SCRIPTS_DIR)/ivpm.mk PHASE2=true VERBOSE=$(VERBOSE) clean
endif

$(BUILD_DIR)/pyyaml.d : $(PYYAML_TGZ)
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)if test ! -d $(LIB_DIR); then mkdir -p $(LIB_DIR); fi
	$(Q)rm -rf $(LIB_DIR)/pyyaml
	$(Q)cd $(BUILD_DIR) ; tar xvzf $(PYYAML_TGZ)
	$(Q)cp -r $(BUILD_DIR)/$(PYYAML_DIR)/lib/yaml $(LIB_DIR)/yaml
	$(Q)touch $@
		
$(PYYAML_TGZ) :
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)wget -O $@ $(PYYAML_URL)
	
$(BUILD_DIR)/jinja2.d : $(JINJA2_TGZ)
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)if test ! -d $(LIB_DIR); then mkdir -p $(LIB_DIR); fi
	$(Q)rm -rf $(LIB_DIR)/jinja2
	$(Q)cd $(BUILD_DIR) ; tar xvzf $(JINJA2_TGZ)
	$(Q)cp -r $(BUILD_DIR)/$(JINJA2_DIR)/jinja2 $(LIB_DIR)/jinja2
	$(Q)touch $@
	
$(JINJA2_TGZ) :
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)wget -O $@ $(JINJA2_URL)

$(BUILD_DIR)/markupsafe.d : $(MARKUPSAFE_TGZ)
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)if test ! -d $(LIB_DIR); then mkdir -p $(LIB_DIR); fi
	$(Q)rm -rf $(LIB_DIR)/markupsafe
	$(Q)cd $(BUILD_DIR) ; tar xvzf $(MARKUPSAFE_TGZ)
	$(Q)cp -r $(BUILD_DIR)/$(MARKUPSAFE_DIR)/markupsafe $(LIB_DIR)/markupsafe
	$(Q)touch $@
	
$(MARKUPSAFE_TGZ) :
	$(Q)if test ! -d `dirname $@`; then mkdir -p `dirname $@`; fi
	$(Q)wget -O $@ $(MARKUPSAFE_URL)

release : $(PACKAGE) $(PACKAGES_DIR)/upload.py
	$(Q)python3 $(PACKAGES_DIR)/upload.py \
		--user mballance --repo vte \
		--key $(GITHUB_API_TOKEN) --version $(version) $(PACKAGE)

$(PACKAGES_DIR)/upload.py :
	$(Q)mkdir -p $(PACKAGES_DIR)
	$(Q)$(WGET) -O $@ $(EDAPACK_BUILD_URL)/raw/master/scripts/upload.py

-include $(PACKAGES_DIR)/packages.mk
