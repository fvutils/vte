#****************************************************************************
#* {{name}} Makefile
#****************************************************************************
SYNTH_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))

include $(PACKAGES_DIR)/packages.mk

ifneq (true,$(VERBOSE))
Q=@
endif

TOP = {{top}}

YOSYS_VARS += TOP SYNTH_DIR

synth.d :
	$(Q)rm -rf output
	$(Q)mkdir -p output
	$(Q)sed $(SYNTH_DIR)/synth.cmd \
		$(foreach v,$(YOSYS_VARS),-e 's%{$(v)}%$($(v))%g') > output/synth.cmd
	$(Q)cd output ; yosys -s synth.cmd
	$(Q)touch $@

clean :
	rm -rf output *.d

