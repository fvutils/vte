#****************************************************************************
#* Makefile for {{name}}
#****************************************************************************
SCRIPTS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
include $(PACKAGES_DIR)/packages.mk
include $(PACKAGES_DIR)/simscripts/mkfiles/plusargs.mk

PLUSARGS += +tool.cocotb

PYTHONPATH:=$(SCRIPTS_DIR)/../../tests/cocotb:$(PYTHONPATH)

# COCOTB_BFM_MODULES += fwrisc_tracer_bfm

TB_MODULES_HDL={{name}}_tb_hdl
VLSIM_CLOCKSPEC += clock={{clk_period}}ns


include $(PACKAGES_DIR)/simscripts/mkfiles/common_sim.mk
include $(PACKAGES_DIR)/packages.mk

