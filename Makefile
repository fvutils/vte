
IVPM_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ifeq (,$(PACKAGES_DIR))
  PACKAGES_DIR := $(IVPM_DIR)/packages
endif

export PACKAGES_DIR

pdf : 
	$(PACKAGES_DIR)/python/bin/sphinx-build -M latexpdf \
		$(IVPM_DIR)/doc/source \
		build

html : 
	$(PACKAGES_DIR)/python/bin/sphinx-build -M html \
		$(IVPM_DIR)/doc/source \
			build

clean :
	rm -rf build 

