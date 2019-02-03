/****************************************************************************
 * {{name}}_tb_hdl.cpp
 ****************************************************************************/
{% set filename = "tb/vl/{{name}}_tb_hdl.cpp" %}
#include "{{name}}_tb_hdl.h"
#include <stdio.h>


{{name}}_tb_hdl::{{name}}_tb_hdl() {
        addClock(top()->clock, {{clk_period}});
}

{{name}}_tb_hdl::~{{name}}_tb_hdl() {

}

void {{name}}_tb_hdl::SetUp() {
}

// Register this top-level with the GoogletestVl system
static GoogletestVlEngineFactory<{{name}}_tb_hdl>         prv_factory;

