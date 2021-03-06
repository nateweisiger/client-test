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


class Search(object):
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
        'daily_email_enabled': 'bool',
        'links': 'object',
        'created': 'datetime',
        'filter': 'Filter',
        'id': 'str',
        'last_executed': 'datetime',
        'name': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'daily_email_enabled': '__daily_email_enabled',
        'links': '_links',
        'created': 'created',
        'filter': 'filter',
        'id': 'id',
        'last_executed': 'last_executed',
        'name': 'name',
        'updated': 'updated'
    }

    def __init__(self, daily_email_enabled=False, links=None, created=None, filter=None, id=None, last_executed=None, name=None, updated=None):  # noqa: E501
        """Search - a model defined in Swagger"""  # noqa: E501

        self._daily_email_enabled = None
        self._links = None
        self._created = None
        self._filter = None
        self._id = None
        self._last_executed = None
        self._name = None
        self._updated = None
        self.discriminator = None

        if daily_email_enabled is not None:
            self.daily_email_enabled = daily_email_enabled
        if links is not None:
            self.links = links
        self.created = created
        self.filter = filter
        self.id = id
        self.last_executed = last_executed
        self.name = name
        self.updated = updated

    @property
    def daily_email_enabled(self):
        """Gets the daily_email_enabled of this Search.  # noqa: E501

        Send a daily email when new results are added.  # noqa: E501

        :return: The daily_email_enabled of this Search.  # noqa: E501
        :rtype: bool
        """
        return self._daily_email_enabled

    @daily_email_enabled.setter
    def daily_email_enabled(self, daily_email_enabled):
        """Sets the daily_email_enabled of this Search.

        Send a daily email when new results are added.  # noqa: E501

        :param daily_email_enabled: The daily_email_enabled of this Search.  # noqa: E501
        :type: bool
        """

        self._daily_email_enabled = daily_email_enabled

    @property
    def links(self):
        """Gets the links of this Search.  # noqa: E501

        Links to related endpoints.  # noqa: E501

        :return: The links of this Search.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Search.

        Links to related endpoints.  # noqa: E501

        :param links: The links of this Search.  # noqa: E501
        :type: object
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this Search.  # noqa: E501

        The date the record was created.  # noqa: E501

        :return: The created of this Search.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Search.

        The date the record was created.  # noqa: E501

        :param created: The created of this Search.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def filter(self):
        """Gets the filter of this Search.  # noqa: E501


        :return: The filter of this Search.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Search.


        :param filter: The filter of this Search.  # noqa: E501
        :type: Filter
        """
        if filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def id(self):
        """Gets the id of this Search.  # noqa: E501

        Saved search identifier.  # noqa: E501

        :return: The id of this Search.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Search.

        Saved search identifier.  # noqa: E501

        :param id: The id of this Search.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search('^.{32}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^.{32}$/`")  # noqa: E501

        self._id = id

    @property
    def last_executed(self):
        """Gets the last_executed of this Search.  # noqa: E501

        The date the search was last executed.  # noqa: E501

        :return: The last_executed of this Search.  # noqa: E501
        :rtype: datetime
        """
        return self._last_executed

    @last_executed.setter
    def last_executed(self, last_executed):
        """Sets the last_executed of this Search.

        The date the search was last executed.  # noqa: E501

        :param last_executed: The last_executed of this Search.  # noqa: E501
        :type: datetime
        """
        if last_executed is None:
            raise ValueError("Invalid value for `last_executed`, must not be `None`")  # noqa: E501

        self._last_executed = last_executed

    @property
    def name(self):
        """Gets the name of this Search.  # noqa: E501

        The name of the saved search.  # noqa: E501

        :return: The name of this Search.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Search.

        The name of the saved search.  # noqa: E501

        :param name: The name of this Search.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search('^.{1,64}$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^.{1,64}$/`")  # noqa: E501

        self._name = name

    @property
    def updated(self):
        """Gets the updated of this Search.  # noqa: E501

        The date the record was updated.  # noqa: E501

        :return: The updated of this Search.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Search.

        The date the record was updated.  # noqa: E501

        :param updated: The updated of this Search.  # noqa: E501
        :type: datetime
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if not isinstance(other, Search):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
