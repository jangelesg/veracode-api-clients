# coding: utf-8

"""
    Veracode Web Application Scanning Configuration Service API

    Web Application Scanning Configuration API Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: veracode@veracode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.v_1_occurrence_api_api import V1OccurrenceApiApi  # noqa: E501
from swagger_client.rest import ApiException


class TestV1OccurrenceApiApi(unittest.TestCase):
    """V1OccurrenceApiApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.v_1_occurrence_api_api.V1OccurrenceApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_analysis_occurrence_by_analysis_occurrence_id_using_get(self):
        """Test case for find_analysis_occurrence_by_analysis_occurrence_id_using_get

        Returns the Dynamic Analysis occurrence for the specified identifier.  # noqa: E501
        """
        pass

    def test_find_analysis_occurrences_by_analysis_id_using_get(self):
        """Test case for find_analysis_occurrences_by_analysis_id_using_get

        Returns a list of occurrences of the Dynamic Analysis. By default, Veracode only returns the occurrences that  started earlier than todays date. Optionally, you can use the status parameter to only return a list of  occurrences of the provided Dynamic Analysis identifier with the specified status(es).   # noqa: E501
        """
        pass

    def test_find_scan_occurence_by_occurrence_id_using_get(self):
        """Test case for find_scan_occurence_by_occurrence_id_using_get

        Returns the URL scan occurrence for the provided URL scan occurrence identifier.  # noqa: E501
        """
        pass

    def test_find_scan_occurrences_by_analysis_occurrence_id_using_get(self):
        """Test case for find_scan_occurrences_by_analysis_occurrence_id_using_get

        Returns a list of completed URL scan occurrences for the specified Dynamic Analysis occurrence.  # noqa: E501
        """
        pass

    def test_find_verification_report_using_get(self):
        """Test case for find_verification_report_using_get

        Returns the Verification Report, which contains connection and authentication details for the specified scan occurrence ID.  # noqa: E501
        """
        pass

    def test_get_runtime_scan_configuration_using_get(self):
        """Test case for get_runtime_scan_configuration_using_get

        Returns the configuration for the specified URL scan occurrence.  # noqa: E501
        """
        pass

    def test_perform_analysis_occurrence_action_using_put(self):
        """Test case for perform_analysis_occurrence_action_using_put

        Performs the specified action on the specified occurrence.  # noqa: E501
        """
        pass

    def test_perform_scan_occurrence_action_using_put(self):
        """Test case for perform_scan_occurrence_action_using_put

        Performs the specified action on the URL scan occurrence.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
