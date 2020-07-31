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


class PythonPackagesCountInfoResponseError(object):
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
        'error': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'error': 'error',
        'parameters': 'parameters'
    }

    def __init__(self, error=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """PythonPackagesCountInfoResponseError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._parameters = None
        self.discriminator = None

        self.error = error
        self.parameters = parameters

    @property
    def error(self):
        """Gets the error of this PythonPackagesCountInfoResponseError.  # noqa: E501

        Error information for user.  # noqa: E501

        :return: The error of this PythonPackagesCountInfoResponseError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PythonPackagesCountInfoResponseError.

        Error information for user.  # noqa: E501

        :param error: The error of this PythonPackagesCountInfoResponseError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def parameters(self):
        """Gets the parameters of this PythonPackagesCountInfoResponseError.  # noqa: E501

        Parameters echoed back to user for debugging.  # noqa: E501

        :return: The parameters of this PythonPackagesCountInfoResponseError.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PythonPackagesCountInfoResponseError.

        Parameters echoed back to user for debugging.  # noqa: E501

        :param parameters: The parameters of this PythonPackagesCountInfoResponseError.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, PythonPackagesCountInfoResponseError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PythonPackagesCountInfoResponseError):
            return True

        return self.to_dict() != other.to_dict()
