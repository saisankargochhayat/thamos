# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from thamos.swagger_client.configuration import Configuration


class AdviseInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'application_stack': 'PythonStack',
        'library_usage': 'AdviseInputLibraryUsage',
        'runtime_environment': 'RuntimeEnvironment'
    }

    attribute_map = {
        'application_stack': 'application_stack',
        'library_usage': 'library_usage',
        'runtime_environment': 'runtime_environment'
    }

    def __init__(self, application_stack=None, library_usage=None, runtime_environment=None, local_vars_configuration=None):  # noqa: E501
        """AdviseInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_stack = None
        self._library_usage = None
        self._runtime_environment = None
        self.discriminator = None

        self.application_stack = application_stack
        if library_usage is not None:
            self.library_usage = library_usage
        if runtime_environment is not None:
            self.runtime_environment = runtime_environment

    @property
    def application_stack(self):
        """Gets the application_stack of this AdviseInput.  # noqa: E501


        :return: The application_stack of this AdviseInput.  # noqa: E501
        :rtype: PythonStack
        """
        return self._application_stack

    @application_stack.setter
    def application_stack(self, application_stack):
        """Sets the application_stack of this AdviseInput.


        :param application_stack: The application_stack of this AdviseInput.  # noqa: E501
        :type: PythonStack
        """
        if self.local_vars_configuration.client_side_validation and application_stack is None:  # noqa: E501
            raise ValueError("Invalid value for `application_stack`, must not be `None`")  # noqa: E501

        self._application_stack = application_stack

    @property
    def library_usage(self):
        """Gets the library_usage of this AdviseInput.  # noqa: E501


        :return: The library_usage of this AdviseInput.  # noqa: E501
        :rtype: AdviseInputLibraryUsage
        """
        return self._library_usage

    @library_usage.setter
    def library_usage(self, library_usage):
        """Sets the library_usage of this AdviseInput.


        :param library_usage: The library_usage of this AdviseInput.  # noqa: E501
        :type: AdviseInputLibraryUsage
        """

        self._library_usage = library_usage

    @property
    def runtime_environment(self):
        """Gets the runtime_environment of this AdviseInput.  # noqa: E501


        :return: The runtime_environment of this AdviseInput.  # noqa: E501
        :rtype: RuntimeEnvironment
        """
        return self._runtime_environment

    @runtime_environment.setter
    def runtime_environment(self, runtime_environment):
        """Sets the runtime_environment of this AdviseInput.


        :param runtime_environment: The runtime_environment of this AdviseInput.  # noqa: E501
        :type: RuntimeEnvironment
        """

        self._runtime_environment = runtime_environment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdviseInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdviseInput):
            return True

        return self.to_dict() != other.to_dict()
