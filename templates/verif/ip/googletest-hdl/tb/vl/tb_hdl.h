/****************************************************************************
 * {{name}}_tb_hdl.h
 ****************************************************************************/
{% set filename = "tb/vl/{{name}}_tb_hdl.h" %}
#ifndef INCLUDED_{{name}}_TB_HDL_H
#define INCLUDED_{{name}}_TB_HDL_H
#include "GoogletestVlEngine.h"
#include "V{{name}}_tb_hdl.h"

using namespace gtest_hdl;

class {{name}}_tb_hdl : public GoogletestVlEngine<V{{name}}_tb_hdl> {
public:
        {{name}}_tb_hdl();

        virtual ~{{name}}_tb_hdl();

        virtual void SetUp();

};


#endif /* INCLUDED_{{name}}_TB_HDL_H */

