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

from lict import *

l1 = 0.1
l2 = 0.2
l3 = Lict(0.3, kind='data')
l4 = Lict(0.4, kind='data')
l5 = Lict(0.5, kind='meta')
l6 = Lict(0.6, kind='meta')

def test_group():
    l = Lict(l1, l2, l3, l4, l5, l6)

    g = l.group('kind')
    assert g.keys()   == [None, 'data', 'meta']
    assert g.values() == [l1, l2, l3, l4, l5, l6]

    d = g.select(None)
    assert d.values() == [l1, l2]

    d = g.select('data')
    assert d.values() == [l3, l4]

    e = g.select('meta')
    assert e.values() == [l5, l6]
