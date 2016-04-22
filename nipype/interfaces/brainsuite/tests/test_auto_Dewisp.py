# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..brainsuite import Dewisp


def test_Dewisp_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputMaskFile=dict(argstr='-i %s',
    mandatory=True,
    ),
    maximumIterations=dict(argstr='-n %d',
    ),
    outputMaskFile=dict(argstr='-o %s',
    genfile=True,
    ),
    sizeThreshold=dict(argstr='-t %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    timer=dict(argstr='--timer',
    ),
    verbosity=dict(argstr='-v %d',
    ),
    )
    inputs = Dewisp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Dewisp_outputs():
    output_map = dict(outputMaskFile=dict(),
    )
    outputs = Dewisp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
