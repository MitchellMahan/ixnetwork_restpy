# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InstructionTypeMiss(Base):
    """NOT DEFINED
    The InstructionTypeMiss class encapsulates a required instructionTypeMiss resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'instructionTypeMiss'
    _SDM_ATT_MAP = {
        'ApplyActions': 'applyActions',
        'ClearActions': 'clearActions',
        'Experimenter': 'experimenter',
        'GoToTable': 'goToTable',
        'Meter': 'meter',
        'WriteActions': 'writeActions',
        'WriteMetadata': 'writeMetadata',
    }

    def __init__(self, parent):
        super(InstructionTypeMiss, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyActions'])
    @ApplyActions.setter
    def ApplyActions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyActions'], value)

    @property
    def ClearActions(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClearActions'])
    @ClearActions.setter
    def ClearActions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClearActions'], value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def GoToTable(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GoToTable'])
    @GoToTable.setter
    def GoToTable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GoToTable'], value)

    @property
    def Meter(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Meter'])
    @Meter.setter
    def Meter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Meter'], value)

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteActions'])
    @WriteActions.setter
    def WriteActions(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteActions'], value)

    @property
    def WriteMetadata(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['WriteMetadata'])
    @WriteMetadata.setter
    def WriteMetadata(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WriteMetadata'], value)

    def update(self, ApplyActions=None, ClearActions=None, Experimenter=None, GoToTable=None, Meter=None, WriteActions=None, WriteMetadata=None):
        """Updates instructionTypeMiss resource on the server.

        Args
        ----
        - ApplyActions (bool): NOT DEFINED
        - ClearActions (bool): NOT DEFINED
        - Experimenter (bool): NOT DEFINED
        - GoToTable (bool): NOT DEFINED
        - Meter (bool): NOT DEFINED
        - WriteActions (bool): NOT DEFINED
        - WriteMetadata (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
