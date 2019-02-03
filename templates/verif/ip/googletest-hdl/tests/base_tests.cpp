/****************************************************************************
 * {{name}}_base_tests.cpp
 ****************************************************************************/
{% set filename = "tests/{{name}}_base_tests.cpp" %}
#include "{{name}}_base_tests.h"

void {{name}}_base_tests::SetUp() {
}

void {{name}}_base_tests::TearDown() {
}

void {{name}}_base_tests::run() {
	GoogletestHdl::run();
}

/**
 * smoke test
 */
TEST_F({{name}}_base_tests,smoke) {
	const CmdlineProcessor &clp = GoogletestHdl::clp();

	run();
}

