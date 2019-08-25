#****************************************************************************
#* {{name}} Makefile
#****************************************************************************
include $(PACKAGES_DIR)/packages.mk
include $(PACKAGES_DIR)/simscripts/mkfiles/plusargs.mk

RUN_TARGETS += run-sby
CHECKER=$(call get_plusarg,CHECKER,$(PLUSARGS))
DEPTH=$(call get_plusarg,DEPTH,$(PLUSARGS))

ifeq (,$(DEPTH))
DEPTH=32
endif

include $(PACKAGES_DIR)/simscripts/mkfiles/common_sim.mk


ifeq (true,$(QUIET))
REDIRECT= >simx.log 2>&1
else
REDIRECT= | tee simx.log 2>&1
endif

VE_DIR := $(abspath $(SIM_DIR)/..)

# List of variables to substitute in the .sby file
SBY_VARS += CHECKER TESTNAME DEPTH VE_DIR

run-sby :
	$(Q)sed $(SIM_DIR)/scripts/{{name}}.sby \
		$(foreach v,$(SBY_VARS),-e 's%{$(v)}%$($(v))%g') > {{name}}.sby
	$(Q)sby -f {{name}}.sby $(REDIRECT)

include $(PACKAGES_DIR)/packages.mk
