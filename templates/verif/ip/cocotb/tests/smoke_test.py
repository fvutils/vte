
{% set filename = "tests/cocotb/{{name}}_tests/smoke_test.py" %} 
import cocotb

@cocotb.test()
def runtest(dut):
    print("TODO: runtest")
    pass

