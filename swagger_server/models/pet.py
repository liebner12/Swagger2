# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, age: int=None):  # noqa: E501
        """Pet - a model defined in Swagger

        :param id: The id of this Pet.  # noqa: E501
        :type id: int
        :param name: The name of this Pet.  # noqa: E501
        :type name: str
        :param age: The age of this Pet.  # noqa: E501
        :type age: int
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'age': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'age': 'age'
        }

        self._id = id
        self._name = name
        self._age = age

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.  # noqa: E501
        :rtype: Pet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Pet.


        :return: The id of this Pet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Pet.


        :param id: The id of this Pet.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Pet.


        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Pet.


        :param name: The name of this Pet.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def age(self) -> int:
        """Gets the age of this Pet.


        :return: The age of this Pet.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this Pet.


        :param age: The age of this Pet.
        :type age: int
        """

        self._age = age
