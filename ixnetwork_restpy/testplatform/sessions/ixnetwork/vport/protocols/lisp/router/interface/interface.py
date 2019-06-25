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


class Interface(Base):
	"""The Interface class encapsulates a user managed interface node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Interface property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'interface'

	def __init__(self, parent):
		super(Interface, self).__init__(parent)

	@property
	def Enabled(self):
		"""If True, it gives details about the interface

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def MapRegisterOrRequestTxInterface(self):
		"""If true, it maps register or requests Tx interface

		Returns:
			bool
		"""
		return self._get_attribute('mapRegisterOrRequestTxInterface')
	@MapRegisterOrRequestTxInterface.setter
	def MapRegisterOrRequestTxInterface(self, value):
		self._set_attribute('mapRegisterOrRequestTxInterface', value)

	@property
	def ProtocolInterfaces(self):
		"""It gives the protocol interfaces

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)
		"""
		return self._get_attribute('protocolInterfaces')
	@ProtocolInterfaces.setter
	def ProtocolInterfaces(self, value):
		self._set_attribute('protocolInterfaces', value)

	def update(self, Enabled=None, MapRegisterOrRequestTxInterface=None, ProtocolInterfaces=None):
		"""Updates a child instance of interface on the server.

		Args:
			Enabled (bool): If True, it gives details about the interface
			MapRegisterOrRequestTxInterface (bool): If true, it maps register or requests Tx interface
			ProtocolInterfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It gives the protocol interfaces

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Enabled=None, MapRegisterOrRequestTxInterface=None, ProtocolInterfaces=None):
		"""Adds a new interface node on the server and retrieves it in this instance.

		Args:
			Enabled (bool): If True, it gives details about the interface
			MapRegisterOrRequestTxInterface (bool): If true, it maps register or requests Tx interface
			ProtocolInterfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It gives the protocol interfaces

		Returns:
			self: This instance with all currently retrieved interface data using find and the newly added interface data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the interface data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Enabled=None, MapRegisterOrRequestTxInterface=None, ProtocolInterfaces=None):
		"""Finds and retrieves interface data from the server.

		All named parameters support regex and can be used to selectively retrieve interface data from the server.
		By default the find method takes no parameters and will retrieve all interface data from the server.

		Args:
			Enabled (bool): If True, it gives details about the interface
			MapRegisterOrRequestTxInterface (bool): If true, it maps register or requests Tx interface
			ProtocolInterfaces (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It gives the protocol interfaces

		Returns:
			self: This instance with matching interface data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of interface data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the interface data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
