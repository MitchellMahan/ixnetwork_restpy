# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class Bfdv6Session(Base):
	"""BFDv6 Session (Device) level Configuration
	The Bfdv6Session class encapsulates a required bfdv6Session resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'bfdv6Session'

	def __init__(self, parent):
		super(Bfdv6Session, self).__init__(parent)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableAutoChooseSourceIp(self):
		"""Selecting this check box enables the ability to configure the source IP address IP of BFD Session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAutoChooseSourceIp')

	@property
	def EnableOVSDBCommunication(self):
		"""Selecting this check box enables the ability to communicate the remote IP and MAC address of BFD Session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOVSDBCommunication')

	@property
	def EnableRemoteDiscriminatorLearned(self):
		"""Selecting this check box enables the ability to configure the remote discriminator for BFD Session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableRemoteDiscriminatorLearned')

	@property
	def LearnedRemoteMac(self):
		"""The learned remote MAC address from controller

		Returns:
			list(str)
		"""
		return self._get_attribute('learnedRemoteMac')

	@property
	def LocalRouterId(self):
		"""The BFD Router ID value, in IPv4 format.

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterId')

	@property
	def MyDiscriminator(self):
		"""The discriminator used locally for the BFD session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('myDiscriminator')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def RemoteDiscriminator(self):
		"""The remote discriminator used by the peer BFD for session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteDiscriminator')

	@property
	def RemoteIp6(self):
		"""The remote IP address used in BFD session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteIp6')

	@property
	def RemoteMac(self):
		"""Remote MAC Address of Peer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteMac')

	@property
	def SessionInfo(self):
		"""Logs additional information about the Session state

		Returns:
			list(str[adminDown|awaitingIp|down|init|maxState|sessDeleted|unknownState|up])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SessionType(self):
		"""Session Type used in BFD session. One of: Single Hop, Multi Hops

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sessionType')

	@property
	def SourceIp6(self):
		"""The source IP address used in BFD session

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIp6')

	@property
	def Vni(self):
		"""Corresponding VXLAN Protocol VNI.

		Returns:
			list(number)
		"""
		return self._get_attribute('vni')

	def update(self, Name=None):
		"""Updates a child instance of bfdv6Session on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, Active=None, EnableAutoChooseSourceIp=None, EnableOVSDBCommunication=None, EnableRemoteDiscriminatorLearned=None, MyDiscriminator=None, RemoteDiscriminator=None, RemoteIp6=None, RemoteMac=None, SessionType=None, SourceIp6=None):
		"""Base class infrastructure that gets a list of bfdv6Session device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			EnableAutoChooseSourceIp (str): optional regex of enableAutoChooseSourceIp
			EnableOVSDBCommunication (str): optional regex of enableOVSDBCommunication
			EnableRemoteDiscriminatorLearned (str): optional regex of enableRemoteDiscriminatorLearned
			MyDiscriminator (str): optional regex of myDiscriminator
			RemoteDiscriminator (str): optional regex of remoteDiscriminator
			RemoteIp6 (str): optional regex of remoteIp6
			RemoteMac (str): optional regex of remoteMac
			SessionType (str): optional regex of sessionType
			SourceIp6 (str): optional regex of sourceIp6

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Activate Session

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		start(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Deactivate Session

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		stop(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
