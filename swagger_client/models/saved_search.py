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

from swagger_client.models.filter import Filter  # noqa: F401,E501


class SavedSearch(object):
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
        'filter': 'Filter',
        'item_types': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'item_types': 'item_types',
        'name': 'name'
    }

    def __init__(self, filter=None, item_types=None, name=None):  # noqa: E501
        """SavedSearch - a model defined in Swagger"""  # noqa: E501

        self._filter = None
        self._item_types = None
        self._name = None
        self.discriminator = None

        self.filter = filter
        self.item_types = item_types
        self.name = name

    @property
    def filter(self):
        """Gets the filter of this SavedSearch.  # noqa: E501


        :return: The filter of this SavedSearch.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SavedSearch.


        :param filter: The filter of this SavedSearch.  # noqa: E501
        :type: Filter
        """
        if filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def item_types(self):
        """Gets the item_types of this SavedSearch.  # noqa: E501

        The ItemTypes to include in the search.  # noqa: E501

        :return: The item_types of this SavedSearch.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_types

    @item_types.setter
    def item_types(self, item_types):
        """Sets the item_types of this SavedSearch.

        The ItemTypes to include in the search.  # noqa: E501

        :param item_types: The item_types of this SavedSearch.  # noqa: E501
        :type: list[str]
        """
        if item_types is None:
            raise ValueError("Invalid value for `item_types`, must not be `None`")  # noqa: E501

        self._item_types = item_types

    @property
    def name(self):
        """Gets the name of this SavedSearch.  # noqa: E501

        The name of this saved search.  # noqa: E501

        :return: The name of this SavedSearch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedSearch.

        The name of this saved search.  # noqa: E501

        :param name: The name of this SavedSearch.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search('^.{1,64}$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^.{1,64}$/`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, SavedSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
