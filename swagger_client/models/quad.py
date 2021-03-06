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

from swagger_client.models.quad__links import QuadLinks  # noqa: F401,E501


class Quad(object):
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
        'links': 'QuadLinks',
        'bbox': 'list[float]',
        'id': 'str',
        'percent_covered': 'float'
    }

    attribute_map = {
        'links': '_links',
        'bbox': 'bbox',
        'id': 'id',
        'percent_covered': 'percent_covered'
    }

    def __init__(self, links=None, bbox=None, id=None, percent_covered=None):  # noqa: E501
        """Quad - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._bbox = None
        self._id = None
        self._percent_covered = None
        self.discriminator = None

        self.links = links
        self.bbox = bbox
        self.id = id
        self.percent_covered = percent_covered

    @property
    def links(self):
        """Gets the links of this Quad.  # noqa: E501


        :return: The links of this Quad.  # noqa: E501
        :rtype: QuadLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Quad.


        :param links: The links of this Quad.  # noqa: E501
        :type: QuadLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def bbox(self):
        """Gets the bbox of this Quad.  # noqa: E501

        The bounding box representing the extent of the quad.  # noqa: E501

        :return: The bbox of this Quad.  # noqa: E501
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this Quad.

        The bounding box representing the extent of the quad.  # noqa: E501

        :param bbox: The bbox of this Quad.  # noqa: E501
        :type: list[float]
        """
        if bbox is None:
            raise ValueError("Invalid value for `bbox`, must not be `None`")  # noqa: E501

        self._bbox = bbox

    @property
    def id(self):
        """Gets the id of this Quad.  # noqa: E501

        Quad identifier.  # noqa: E501

        :return: The id of this Quad.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Quad.

        Quad identifier.  # noqa: E501

        :param id: The id of this Quad.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def percent_covered(self):
        """Gets the percent_covered of this Quad.  # noqa: E501

        The percentage of the GeoTIFF pixels that are not no-data values.  # noqa: E501

        :return: The percent_covered of this Quad.  # noqa: E501
        :rtype: float
        """
        return self._percent_covered

    @percent_covered.setter
    def percent_covered(self, percent_covered):
        """Sets the percent_covered of this Quad.

        The percentage of the GeoTIFF pixels that are not no-data values.  # noqa: E501

        :param percent_covered: The percent_covered of this Quad.  # noqa: E501
        :type: float
        """
        if percent_covered is None:
            raise ValueError("Invalid value for `percent_covered`, must not be `None`")  # noqa: E501

        self._percent_covered = percent_covered

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
        if not isinstance(other, Quad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
