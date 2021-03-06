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

from swagger_client.models.geo_json_geometry import GeoJSONGeometry  # noqa: F401,E501


class GeoJSONFeature(object):
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
        'geometry': 'GeoJSONGeometry',
        'properties': 'object'
    }

    attribute_map = {
        'geometry': 'geometry',
        'properties': 'properties'
    }

    def __init__(self, geometry=None, properties=None):  # noqa: E501
        """GeoJSONFeature - a model defined in Swagger"""  # noqa: E501

        self._geometry = None
        self._properties = None
        self.discriminator = None

        self.geometry = geometry
        self.properties = properties

    @property
    def geometry(self):
        """Gets the geometry of this GeoJSONFeature.  # noqa: E501


        :return: The geometry of this GeoJSONFeature.  # noqa: E501
        :rtype: GeoJSONGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this GeoJSONFeature.


        :param geometry: The geometry of this GeoJSONFeature.  # noqa: E501
        :type: GeoJSONGeometry
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

    @property
    def properties(self):
        """Gets the properties of this GeoJSONFeature.  # noqa: E501


        :return: The properties of this GeoJSONFeature.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GeoJSONFeature.


        :param properties: The properties of this GeoJSONFeature.  # noqa: E501
        :type: object
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, GeoJSONFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
