# Copyright 2017 Chi-kwan Chan
# Copyright 2017 Harvard-Smithsonian Center for Astrophysics
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from metainer import *
import pytest

def test_append():
    m = Metainer()

    m.append('meta', 0.1)
    assert m == [('meta', 0.1)]

    m.append(None, 0.2)
    assert m == [('meta', 0.1), (None, 0.2)]

    with pytest.raises(TypeError) as e:
        m.append([], 0.3)
    assert m == [('meta', 0.1), (None, 0.2)]
    assert str(e.value) == "unhashable type: 'list'"