# Copyright 2024 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest
import numpy as np
import cirq
from cirq.transformers.gauge_compiling.gauge_compiling_test_utils import GaugeTester
from cirq.transformers import GaugeTransformer, GaugeSelector, ConstantGauge


class ExampleGate(cirq.testing.TwoQubitGate):
    unitary = cirq.unitary(cirq.CZ**0.123)

    def _unitary_(self) -> np.ndarray:
        return self.unitary


_EXAMPLE_TARGET = ExampleGate()

_GOOD_TRANSFORMER = GaugeTransformer(
    target=_EXAMPLE_TARGET,
    gauge_selector=GaugeSelector(gauges=[ConstantGauge(two_qubit_gate=_EXAMPLE_TARGET)]),
)

_BAD_TRANSFORMER = GaugeTransformer(
    target=_EXAMPLE_TARGET,
    gauge_selector=GaugeSelector(
        gauges=[ConstantGauge(two_qubit_gate=_EXAMPLE_TARGET, pre_q0=cirq.X)]
    ),
)


class TestValidTransformer(GaugeTester):
    two_qubit_gate = _EXAMPLE_TARGET
    gauge_transformer = _GOOD_TRANSFORMER


@pytest.mark.xfail(strict=True)
class TestInvalidTransformer(GaugeTester):
    two_qubit_gate = _EXAMPLE_TARGET
    gauge_transformer = _BAD_TRANSFORMER
