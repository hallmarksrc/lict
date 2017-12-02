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

class Lict(list):
    """Lict

    `Lict` is a hybrid list-dict container.  It supports
    metadata-based object management by allowing its keys/names to be
    transformed seamlessly among hierarchical, flat, and mixed
    structures.  Its simple, flexible, and transformable design is
    ideal for building interpolatable python classes.

    """

    def __init__(self, *args, **kwargs):
        for arg in args:
            self.append(arg)
        for k, v in kwargs.items():
            self.append(k, v)

    def append(self, *args, **kwargs):
        if   len(args)   == 1:
            key, value = None, args[0]
        elif len(args)   == 2:
            key, value = args
        elif len(kwargs) == 1:
            key, value = next(iter(kwargs.items()))
        else:
            raise ValueError("append() takes exactly one metakey:metadata pair")

        hash(key)
        super().append((key, value))