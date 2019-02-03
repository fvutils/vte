{% set filename = "tests/{{name}}_tests.mk" %}

{{name}}_TESTS_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

ifneq (1,$(RULES))

SRC_DIRS += $({{name}}_TESTS_DIR)
# TODO: Add source directories for each relevant sub-directory

{{name}}_TESTS_SRC := $(notdir $(wildcard $({{name}}_TESTS_DIR)/*.cpp))

else # Rules


lib{{name}}_tests.o : $({{name}}_TESTS_SRC:.cpp=.o)
	$(Q)$(LD) -r -o $@ $({{name}}_TESTS_SRC:.cpp=.o)
        

endif
