#****************************************************************************
#* Makefile for {{name}}
#****************************************************************************
SCRIPTS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
include $(PACKAGES_DIR)/packages.mk
include $(PACKAGES_DIR)/simscripts/mkfiles/plusargs.mk


MK_INCLUDES += $(SCRIPTS_DIR)/../../tests/{{name}}_tests.mk
MK_INCLUDES += $(SCRIPTS_DIR)/../../tb/vl/{{name}}_tb_vl.mk

MK_INCLUDES += $(GOOGLETEST_HDL)/src/sv/googletest_hdl_sv.mk
MK_INCLUDES += $(GOOGLETEST_HDL)/src/vl/googletest_hdl_vl.mk

SRC_DIRS += $(SCRIPTS_DIR)/../tb

TB_MODULES_HDL={{name}}_tb_hdl
TB_MODULES_HVL={{name}}_tb_hvl

ifeq (vl,$(SIM))
  CXXFLAGS += -I$(BUILDDIR)/obj_dir
  DPI_OBJS_LIBS += libgoogletest-hdl-vl.o lib{{name}}_tb_vl.o
endif

DPI_OBJS_LIBS += $(GVM_OBJS_LIBS)
DPI_OBJS_LIBS += lib{{name}}_tests.o libgoogletest-hdl.o libgoogletest.o

ifeq (ms,$(SIM))
DPI_OBJS_LIBS += libgoogletest-hdl-sv.o
endif


include $(PACKAGES_DIR)/simscripts/mkfiles/common_sim.mk

include $(PACKAGES_DIR)/packages.mk
