# -------------------------------------------------------------------------

# Copyright (c) 2023 General Motors GTO LLC

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# -------------------------------------------------------------------------

from enum import Enum, unique


@unique
class UMessageType(Enum):
    """
    uProtocol defines message types. Using the message type, validation can be performed to ensure transport validity
    of the data in the UAttributes.
    """
    PUBLISH = (0, "pub.v1")  # Publish or notification event
    REQUEST = (1, "req.v1")  # Request
    RESPONSE = (2, "res.v1")  # Response

    def __init__(self, value: int, name: str):
        self.int_value = value
        self.string_value = name

    def int_value(self):
        return self.int_value

    def string_value(self):
        return self.string_value

    @classmethod
    def from_int(cls, value: int):
        """
        Find the Message type from a numeric value. Mind you, it might not exist.<br><br>
        @param value:numeric message type.
        @return:Returns the UMessageType matching the numeric value.
        """
        for item in cls:
            if item.int_value == value:
                return item
        return None

    @classmethod
    def from_string(cls, value: str):
        """
        Find the Message type from a string value. Mind you, it might not exist.
        @param value:string message type.
        @return:Returns the UMessageType matching the string value.
        """
        for item in cls:
            if item.string_value == value:
                return item
        return None
