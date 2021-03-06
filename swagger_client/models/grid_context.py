# coding: utf-8

"""
    Planet API

    Top level description of the API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GridContext(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'quad_pattern': 'str',
        'quad_size': 'int',
        'resolution': 'float'
    }

    attribute_map = {
        'quad_pattern': 'quad_pattern',
        'quad_size': 'quad_size',
        'resolution': 'resolution'
    }

    def __init__(self, quad_pattern=None, quad_size=None, resolution=None):  # noqa: E501
        """GridContext - a model defined in Swagger"""  # noqa: E501

        self._quad_pattern = None
        self._quad_size = None
        self._resolution = None
        self.discriminator = None

        if quad_pattern is not None:
            self.quad_pattern = quad_pattern
        if quad_size is not None:
            self.quad_size = quad_size
        if resolution is not None:
            self.resolution = resolution

    @property
    def quad_pattern(self):
        """Gets the quad_pattern of this GridContext.  # noqa: E501

        Pattern to map quad coord to quad id.  # noqa: E501

        :return: The quad_pattern of this GridContext.  # noqa: E501
        :rtype: str
        """
        return self._quad_pattern

    @quad_pattern.setter
    def quad_pattern(self, quad_pattern):
        """Sets the quad_pattern of this GridContext.

        Pattern to map quad coord to quad id.  # noqa: E501

        :param quad_pattern: The quad_pattern of this GridContext.  # noqa: E501
        :type: str
        """

        self._quad_pattern = quad_pattern

    @property
    def quad_size(self):
        """Gets the quad_size of this GridContext.  # noqa: E501

        The size of the square quad in pixels.  # noqa: E501

        :return: The quad_size of this GridContext.  # noqa: E501
        :rtype: int
        """
        return self._quad_size

    @quad_size.setter
    def quad_size(self, quad_size):
        """Sets the quad_size of this GridContext.

        The size of the square quad in pixels.  # noqa: E501

        :param quad_size: The quad_size of this GridContext.  # noqa: E501
        :type: int
        """

        self._quad_size = quad_size

    @property
    def resolution(self):
        """Gets the resolution of this GridContext.  # noqa: E501

        The resolution of the maximum zoom level in meters.  # noqa: E501

        :return: The resolution of this GridContext.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this GridContext.

        The resolution of the maximum zoom level in meters.  # noqa: E501

        :param resolution: The resolution of this GridContext.  # noqa: E501
        :type: float
        """

        self._resolution = resolution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, GridContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
