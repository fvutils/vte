/****************************************************************************
 * {{name}}_base_tests.h
 ****************************************************************************/
{% set filename = "tests/{{name}}_base_tests.h" %}
#pragma once
#include "gtest/gtest.h"
#include "GoogletestHdl.h"

class {{name}}_base_tests : public ::testing::Test {
public:

	virtual void SetUp();

	virtual void TearDown();

	virtual void run();

};

