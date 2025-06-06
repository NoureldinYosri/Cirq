# Copyright 2025 The Cirq Developers
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

from __future__ import annotations

import cirq
from cirq.transformers.gauge_compiling.cphase_gauge import CPhaseGaugeTransformer
from cirq.transformers.gauge_compiling.gauge_compiling_test_utils import GaugeTester


class TestCPhaseGauge_0_3(GaugeTester):
    two_qubit_gate = cirq.CZ**0.3
    gauge_transformer = CPhaseGaugeTransformer


class TestCPhaseGauge_m0_3(GaugeTester):
    two_qubit_gate = cirq.CZ ** (-0.3)
    gauge_transformer = CPhaseGaugeTransformer


class TestCPhaseGauge_0_1(GaugeTester):
    two_qubit_gate = cirq.CZ**0.1
    gauge_transformer = CPhaseGaugeTransformer


class TestCPhaseGauge_m0_1(GaugeTester):
    two_qubit_gate = cirq.CZ ** (-0.1)
    gauge_transformer = CPhaseGaugeTransformer


class TestCPhaseGauge_0_7(GaugeTester):
    two_qubit_gate = cirq.CZ**0.7
    gauge_transformer = CPhaseGaugeTransformer
