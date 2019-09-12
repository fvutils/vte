#****************************************************************************
#* Synthesis command script
#****************************************************************************

# TODO: Specify source files
# read_verilog

hierarchy -check

# high-level synthesis
proc; opt; fsm; opt; memory; opt

show -format ps

synth_ice40 -top {TOP} -blif {TOP}.blif -abc2 -json {TOP}.json

