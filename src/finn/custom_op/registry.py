# Copyright (c) 2020 Xilinx, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of Xilinx nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from finn.custom_op.debugmarker import DebugMarker
from finn.custom_op.im2col import Im2Col
from finn.custom_op.maxpoolnhwc import MaxPoolNHWC
from finn.custom_op.multithreshold import MultiThreshold
from finn.custom_op.quantavgpool2d import QuantAvgPool2d
from finn.custom_op.streamingdataflowpartition import StreamingDataflowPartition
from finn.custom_op.xnorpopcount import XnorPopcountMatMul

# create a mapping of all known CustomOp names and classes
# make sure new CustomOp subclasses are imported here so that they get
# registered and plug in correctly into the infrastructure
custom_op = {}

custom_op["DebugMarker"] = DebugMarker
custom_op["QuantAvgPool2d"] = QuantAvgPool2d
custom_op["MaxPoolNHWC"] = MaxPoolNHWC
custom_op["StreamingDataflowPartition"] = StreamingDataflowPartition
custom_op["MultiThreshold"] = MultiThreshold
custom_op["XnorPopcountMatMul"] = XnorPopcountMatMul
custom_op["Im2Col"] = Im2Col


def getCustomOp(node):
    "Return a FINN CustomOp instance for the given ONNX node, if it exists."
    op_type = node.op_type
    try:
        # lookup op_type in registry of CustomOps
        inst = custom_op[op_type](node)
        return inst
    except KeyError:
        # exception if op_type is not supported
        raise Exception("Custom op_type %s is currently not supported." % op_type)
