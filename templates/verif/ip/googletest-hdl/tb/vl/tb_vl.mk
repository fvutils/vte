{% set filename = "tb/vl/{{name}}_tb_vl.mk" %}

{{name}}_TB_VL_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

ifneq (1,$(RULES))

ifeq (vl,$(SIM))
SRC_DIRS += $({{name}}_TB_VL_DIR)
endif

{{name}}_TB_VL_SRC_FILES=$(wildcard $({{name}}_TB_VL_DIR)/*.cpp)
{{name}}_TB_VL_SRC=$(notdir $({{name}}_TB_VL_SRC_FILES))

else # Rules

# Compilation of the testbench wrapper requires the
# translated header files produced by vl_translate.d
lib{{name}}_tb_vl.o : {{name}}_tb_hdl.cpp vl_translate.d
	$(Q)$(CXX) -c -o $@ $(CXXFLAGS) $(filter %.cpp,$(^))

endif

