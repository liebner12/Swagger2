# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPetController(BaseTestCase):
    """PetController integration test stubs"""

    def test_add_pet(self):
        """Test case for add_pet

        Add a new pet
        """
        body = Pet()
        response = self.client.open(
            '/v2/pets',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_pets(self):
        """Test case for get_all_pets

        Get all pets
        """
        response = self.client.open(
            '/v2/pets',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pet_by_id(self):
        """Test case for get_pet_by_id

        Find pet by ID
        """
        response = self.client.open(
            '/v2/pets/{petId}'.format(petId=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
