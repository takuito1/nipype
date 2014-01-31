# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.vista.vista import VtoMat
def test_VtoMat_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(hash_files=False,
    name_template='%s.mat',
    name_source=['in_file'],
    keep_extension=False,
    position=-1,
    argstr='-out %s',
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(nohash=True,
    mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=1,
    mandatory=True,
    argstr='-in %s',
    ),
    )
    inputs = VtoMat.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_VtoMat_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = VtoMat.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value