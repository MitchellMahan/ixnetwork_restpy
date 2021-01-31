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


class Router(Base):
    """This object represents a simulated PIM-SM router which holds a list of interfaces associated with the simulated router.
    The Router class encapsulates a list of router resources that are managed by the user.
    A list of resources can be retrieved from the server using the Router.find() method.
    The list can be managed by using the Router.add() and Router.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'router'
    _SDM_ATT_MAP = {
        'DataMdtInterval': 'dataMdtInterval',
        'DataMdtTimeOut': 'dataMdtTimeOut',
        'DrPriority': 'drPriority',
        'Enabled': 'enabled',
        'JoinPruneHoldTime': 'joinPruneHoldTime',
        'JoinPruneInterval': 'joinPruneInterval',
        'RouterId': 'routerId',
        'RpDiscoveryMode': 'rpDiscoveryMode',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Router, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_97fe2baaa3bd9a0d65fcae0b6ca30b80.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_97fe2baaa3bd9a0d65fcae0b6ca30b80 import Interface
        return Interface(self)

    @property
    def DataMdtInterval(self):
        """
        Returns
        -------
        - number: The time interval, in seconds, between transmissions of Data MDT Join TLV messages by the source PE Router. (default = 60)
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataMdtInterval'])
    @DataMdtInterval.setter
    def DataMdtInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataMdtInterval'], value)

    @property
    def DataMdtTimeOut(self):
        """
        Returns
        -------
        - number: The Data MDT hold time, in seconds. If a PE router connected to a receiver does not receive a Data MDT Join TLV message within this time period, it will leave the Data MDT group. (default = 180)
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataMdtTimeOut'])
    @DataMdtTimeOut.setter
    def DataMdtTimeOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DataMdtTimeOut'], value)

    @property
    def DrPriority(self):
        """
        Returns
        -------
        - number: The Designated Router (DR) priority, used for DR election.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DrPriority'])
    @DrPriority.setter
    def DrPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DrPriority'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the router's simulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def JoinPruneHoldTime(self):
        """
        Returns
        -------
        - number: The amount of time that neighbor routers should hold a received Join state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinPruneHoldTime'])
    @JoinPruneHoldTime.setter
    def JoinPruneHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinPruneHoldTime'], value)

    @property
    def JoinPruneInterval(self):
        """
        Returns
        -------
        - number: The interval between transmitted Join/Prune messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JoinPruneInterval'])
    @JoinPruneInterval.setter
    def JoinPruneInterval(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JoinPruneInterval'], value)

    @property
    def RouterId(self):
        """
        Returns
        -------
        - str: The ID of the router, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RouterId'])
    @RouterId.setter
    def RouterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RouterId'], value)

    @property
    def RpDiscoveryMode(self):
        """
        Returns
        -------
        - str(manual | auto): Sets the discovery mode of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RpDiscoveryMode'])
    @RpDiscoveryMode.setter
    def RpDiscoveryMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RpDiscoveryMode'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    def update(self, DataMdtInterval=None, DataMdtTimeOut=None, DrPriority=None, Enabled=None, JoinPruneHoldTime=None, JoinPruneInterval=None, RouterId=None, RpDiscoveryMode=None, TrafficGroupId=None):
        """Updates router resource on the server.

        Args
        ----
        - DataMdtInterval (number): The time interval, in seconds, between transmissions of Data MDT Join TLV messages by the source PE Router. (default = 60)
        - DataMdtTimeOut (number): The Data MDT hold time, in seconds. If a PE router connected to a receiver does not receive a Data MDT Join TLV message within this time period, it will leave the Data MDT group. (default = 180)
        - DrPriority (number): The Designated Router (DR) priority, used for DR election.
        - Enabled (bool): Enables or disables the router's simulation.
        - JoinPruneHoldTime (number): The amount of time that neighbor routers should hold a received Join state.
        - JoinPruneInterval (number): The interval between transmitted Join/Prune messages.
        - RouterId (str): The ID of the router, in IPv4 format.
        - RpDiscoveryMode (str(manual | auto)): Sets the discovery mode of the router.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, DataMdtInterval=None, DataMdtTimeOut=None, DrPriority=None, Enabled=None, JoinPruneHoldTime=None, JoinPruneInterval=None, RouterId=None, RpDiscoveryMode=None, TrafficGroupId=None):
        """Adds a new router resource on the server and adds it to the container.

        Args
        ----
        - DataMdtInterval (number): The time interval, in seconds, between transmissions of Data MDT Join TLV messages by the source PE Router. (default = 60)
        - DataMdtTimeOut (number): The Data MDT hold time, in seconds. If a PE router connected to a receiver does not receive a Data MDT Join TLV message within this time period, it will leave the Data MDT group. (default = 180)
        - DrPriority (number): The Designated Router (DR) priority, used for DR election.
        - Enabled (bool): Enables or disables the router's simulation.
        - JoinPruneHoldTime (number): The amount of time that neighbor routers should hold a received Join state.
        - JoinPruneInterval (number): The interval between transmitted Join/Prune messages.
        - RouterId (str): The ID of the router, in IPv4 format.
        - RpDiscoveryMode (str(manual | auto)): Sets the discovery mode of the router.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved router resources using find and the newly added router resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained router resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DataMdtInterval=None, DataMdtTimeOut=None, DrPriority=None, Enabled=None, JoinPruneHoldTime=None, JoinPruneInterval=None, RouterId=None, RpDiscoveryMode=None, TrafficGroupId=None):
        """Finds and retrieves router resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve router resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all router resources from the server.

        Args
        ----
        - DataMdtInterval (number): The time interval, in seconds, between transmissions of Data MDT Join TLV messages by the source PE Router. (default = 60)
        - DataMdtTimeOut (number): The Data MDT hold time, in seconds. If a PE router connected to a receiver does not receive a Data MDT Join TLV message within this time period, it will leave the Data MDT group. (default = 180)
        - DrPriority (number): The Designated Router (DR) priority, used for DR election.
        - Enabled (bool): Enables or disables the router's simulation.
        - JoinPruneHoldTime (number): The amount of time that neighbor routers should hold a received Join state.
        - JoinPruneInterval (number): The interval between transmitted Join/Prune messages.
        - RouterId (str): The ID of the router, in IPv4 format.
        - RpDiscoveryMode (str(manual | auto)): Sets the discovery mode of the router.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this emulated router is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching router resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of router data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the router resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
