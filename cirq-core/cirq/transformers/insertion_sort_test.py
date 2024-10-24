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
import cirq
import cirq.transformers
from cirq.transformers import insertion_sort


@pytest.mark.parametrize('qubit_threshold', [1, 64])
def test_insertion_sort(qubit_threshold):
    insertion_sort._MAX_QUBIT_COUNT_FOR_MASK = qubit_threshold
    c = cirq.Circuit(
        cirq.CZ(cirq.q(2), cirq.q(1)),
        cirq.CZ(cirq.q(2), cirq.q(4)),
        cirq.CZ(cirq.q(0), cirq.q(1)),
        cirq.CZ(cirq.q(2), cirq.q(1)),
    )
    sorted_circuit = cirq.transformers.insertion_sort_transformer(c)
    assert sorted_circuit == cirq.Circuit(
        cirq.CZ(cirq.q(0), cirq.q(1)),
        cirq.CZ(cirq.q(2), cirq.q(1)),
        cirq.CZ(cirq.q(2), cirq.q(1)),
        cirq.CZ(cirq.q(2), cirq.q(4)),
    )
