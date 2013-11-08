# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.utils import AverageAffineTransform
def test_AverageAffineTransform_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    output_affine_transform=dict(position=1,
    mandatory=True,
    argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    transforms=dict(argstr='%s',
    mandatory=True,
    position=3,
    ),
    dimension=dict(mandatory=True,
    usedefault=False,
    position=0,
    argstr='%d',
    ),
    )
    inputs = AverageAffineTransform.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_AverageAffineTransform_outputs():
    output_map = dict(affine_transform=dict(),
    )
    outputs = AverageAffineTransform.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value