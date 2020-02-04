# coding: utf-8

"""
    Veracode Web Application Scanning Configuration Service API

    Web Application Scanning Configuration API Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: veracode@veracode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DetailedScan(object):
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
        'scan_id': 'str',
        'org': 'str',
        'target_url': 'str',
        'analysis_id': 'str',
        'analysis_name': 'str',
        'internal_scan_configuration': 'InternalScanConfiguration',
        'last_verified_by_prescan': 'bool',
        'last_verified_on': 'str',
        'latest_occurrence_status': 'ScanOccurrenceStatus',
        'latest_occurrence_verifications': 'list[ScanVerification]',
        'linked_platform_app_uuid': 'str',
        'linked_platform_app_name': 'str',
        'scan_contact_info': 'ContactInformation',
        'scan_locked': 'bool',
        'scan_locked_on': 'str',
        'created_on': 'str',
        'last_modified_on': 'str',
        'links': 'list[Link]',
        'capabilities': 'list[str]'
    }

    attribute_map = {
        'scan_id': 'scan_id',
        'org': 'org',
        'target_url': 'target_url',
        'analysis_id': 'analysis_id',
        'analysis_name': 'analysis_name',
        'internal_scan_configuration': 'internal_scan_configuration',
        'last_verified_by_prescan': 'last_verified_by_prescan',
        'last_verified_on': 'last_verified_on',
        'latest_occurrence_status': 'latest_occurrence_status',
        'latest_occurrence_verifications': 'latest_occurrence_verifications',
        'linked_platform_app_uuid': 'linked_platform_app_uuid',
        'linked_platform_app_name': 'linked_platform_app_name',
        'scan_contact_info': 'scan_contact_info',
        'scan_locked': 'scan_locked',
        'scan_locked_on': 'scan_locked_on',
        'created_on': 'created_on',
        'last_modified_on': 'last_modified_on',
        'links': '_links',
        'capabilities': 'capabilities'
    }

    def __init__(self, scan_id=None, org=None, target_url=None, analysis_id=None, analysis_name=None, internal_scan_configuration=None, last_verified_by_prescan=None, last_verified_on=None, latest_occurrence_status=None, latest_occurrence_verifications=None, linked_platform_app_uuid=None, linked_platform_app_name=None, scan_contact_info=None, scan_locked=None, scan_locked_on=None, created_on=None, last_modified_on=None, links=None, capabilities=None):  # noqa: E501
        """DetailedScan - a model defined in Swagger"""  # noqa: E501

        self._scan_id = None
        self._org = None
        self._target_url = None
        self._analysis_id = None
        self._analysis_name = None
        self._internal_scan_configuration = None
        self._last_verified_by_prescan = None
        self._last_verified_on = None
        self._latest_occurrence_status = None
        self._latest_occurrence_verifications = None
        self._linked_platform_app_uuid = None
        self._linked_platform_app_name = None
        self._scan_contact_info = None
        self._scan_locked = None
        self._scan_locked_on = None
        self._created_on = None
        self._last_modified_on = None
        self._links = None
        self._capabilities = None
        self.discriminator = None

        if scan_id is not None:
            self.scan_id = scan_id
        if org is not None:
            self.org = org
        if target_url is not None:
            self.target_url = target_url
        if analysis_id is not None:
            self.analysis_id = analysis_id
        if analysis_name is not None:
            self.analysis_name = analysis_name
        if internal_scan_configuration is not None:
            self.internal_scan_configuration = internal_scan_configuration
        if last_verified_by_prescan is not None:
            self.last_verified_by_prescan = last_verified_by_prescan
        if last_verified_on is not None:
            self.last_verified_on = last_verified_on
        if latest_occurrence_status is not None:
            self.latest_occurrence_status = latest_occurrence_status
        if latest_occurrence_verifications is not None:
            self.latest_occurrence_verifications = latest_occurrence_verifications
        if linked_platform_app_uuid is not None:
            self.linked_platform_app_uuid = linked_platform_app_uuid
        if linked_platform_app_name is not None:
            self.linked_platform_app_name = linked_platform_app_name
        if scan_contact_info is not None:
            self.scan_contact_info = scan_contact_info
        if scan_locked is not None:
            self.scan_locked = scan_locked
        if scan_locked_on is not None:
            self.scan_locked_on = scan_locked_on
        if created_on is not None:
            self.created_on = created_on
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if links is not None:
            self.links = links
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def scan_id(self):
        """Gets the scan_id of this DetailedScan.  # noqa: E501

        Identifier of the URL scan.  # noqa: E501

        :return: The scan_id of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._scan_id

    @scan_id.setter
    def scan_id(self, scan_id):
        """Sets the scan_id of this DetailedScan.

        Identifier of the URL scan.  # noqa: E501

        :param scan_id: The scan_id of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._scan_id = scan_id

    @property
    def org(self):
        """Gets the org of this DetailedScan.  # noqa: E501

        Organization identifier.  # noqa: E501

        :return: The org of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this DetailedScan.

        Organization identifier.  # noqa: E501

        :param org: The org of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def target_url(self):
        """Gets the target_url of this DetailedScan.  # noqa: E501

        Target URL of the scan.  # noqa: E501

        :return: The target_url of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this DetailedScan.

        Target URL of the scan.  # noqa: E501

        :param target_url: The target_url of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

    @property
    def analysis_id(self):
        """Gets the analysis_id of this DetailedScan.  # noqa: E501

        Identifier of the Dynamic Analysis this URL scan is a part of.  # noqa: E501

        :return: The analysis_id of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this DetailedScan.

        Identifier of the Dynamic Analysis this URL scan is a part of.  # noqa: E501

        :param analysis_id: The analysis_id of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._analysis_id = analysis_id

    @property
    def analysis_name(self):
        """Gets the analysis_name of this DetailedScan.  # noqa: E501

        Name of the Dynamic Analysis this URL scan is a part of.  # noqa: E501

        :return: The analysis_name of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._analysis_name

    @analysis_name.setter
    def analysis_name(self, analysis_name):
        """Sets the analysis_name of this DetailedScan.

        Name of the Dynamic Analysis this URL scan is a part of.  # noqa: E501

        :param analysis_name: The analysis_name of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._analysis_name = analysis_name

    @property
    def internal_scan_configuration(self):
        """Gets the internal_scan_configuration of this DetailedScan.  # noqa: E501

        Configuration data for the internal scanning gateway and endpoint, if this scan is an internal scan.  # noqa: E501

        :return: The internal_scan_configuration of this DetailedScan.  # noqa: E501
        :rtype: InternalScanConfiguration
        """
        return self._internal_scan_configuration

    @internal_scan_configuration.setter
    def internal_scan_configuration(self, internal_scan_configuration):
        """Sets the internal_scan_configuration of this DetailedScan.

        Configuration data for the internal scanning gateway and endpoint, if this scan is an internal scan.  # noqa: E501

        :param internal_scan_configuration: The internal_scan_configuration of this DetailedScan.  # noqa: E501
        :type: InternalScanConfiguration
        """

        self._internal_scan_configuration = internal_scan_configuration

    @property
    def last_verified_by_prescan(self):
        """Gets the last_verified_by_prescan of this DetailedScan.  # noqa: E501

        True, if the last verification was done using a prescan.  # noqa: E501

        :return: The last_verified_by_prescan of this DetailedScan.  # noqa: E501
        :rtype: bool
        """
        return self._last_verified_by_prescan

    @last_verified_by_prescan.setter
    def last_verified_by_prescan(self, last_verified_by_prescan):
        """Sets the last_verified_by_prescan of this DetailedScan.

        True, if the last verification was done using a prescan.  # noqa: E501

        :param last_verified_by_prescan: The last_verified_by_prescan of this DetailedScan.  # noqa: E501
        :type: bool
        """

        self._last_verified_by_prescan = last_verified_by_prescan

    @property
    def last_verified_on(self):
        """Gets the last_verified_on of this DetailedScan.  # noqa: E501

        Date and time this configuration was last verified using a prescan occurrence.  # noqa: E501

        :return: The last_verified_on of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._last_verified_on

    @last_verified_on.setter
    def last_verified_on(self, last_verified_on):
        """Sets the last_verified_on of this DetailedScan.

        Date and time this configuration was last verified using a prescan occurrence.  # noqa: E501

        :param last_verified_on: The last_verified_on of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._last_verified_on = last_verified_on

    @property
    def latest_occurrence_status(self):
        """Gets the latest_occurrence_status of this DetailedScan.  # noqa: E501

        Status of the latest occurrence of this URL scan.  # noqa: E501

        :return: The latest_occurrence_status of this DetailedScan.  # noqa: E501
        :rtype: ScanOccurrenceStatus
        """
        return self._latest_occurrence_status

    @latest_occurrence_status.setter
    def latest_occurrence_status(self, latest_occurrence_status):
        """Sets the latest_occurrence_status of this DetailedScan.

        Status of the latest occurrence of this URL scan.  # noqa: E501

        :param latest_occurrence_status: The latest_occurrence_status of this DetailedScan.  # noqa: E501
        :type: ScanOccurrenceStatus
        """

        self._latest_occurrence_status = latest_occurrence_status

    @property
    def latest_occurrence_verifications(self):
        """Gets the latest_occurrence_verifications of this DetailedScan.  # noqa: E501

        List of the verifications completed for this URL scan in the latest occurrence.  # noqa: E501

        :return: The latest_occurrence_verifications of this DetailedScan.  # noqa: E501
        :rtype: list[ScanVerification]
        """
        return self._latest_occurrence_verifications

    @latest_occurrence_verifications.setter
    def latest_occurrence_verifications(self, latest_occurrence_verifications):
        """Sets the latest_occurrence_verifications of this DetailedScan.

        List of the verifications completed for this URL scan in the latest occurrence.  # noqa: E501

        :param latest_occurrence_verifications: The latest_occurrence_verifications of this DetailedScan.  # noqa: E501
        :type: list[ScanVerification]
        """

        self._latest_occurrence_verifications = latest_occurrence_verifications

    @property
    def linked_platform_app_uuid(self):
        """Gets the linked_platform_app_uuid of this DetailedScan.  # noqa: E501

        UUID of the Veracode Platform application linked to the URL scan.  # noqa: E501

        :return: The linked_platform_app_uuid of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._linked_platform_app_uuid

    @linked_platform_app_uuid.setter
    def linked_platform_app_uuid(self, linked_platform_app_uuid):
        """Sets the linked_platform_app_uuid of this DetailedScan.

        UUID of the Veracode Platform application linked to the URL scan.  # noqa: E501

        :param linked_platform_app_uuid: The linked_platform_app_uuid of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._linked_platform_app_uuid = linked_platform_app_uuid

    @property
    def linked_platform_app_name(self):
        """Gets the linked_platform_app_name of this DetailedScan.  # noqa: E501

        Name of the linked application in the application portfoliio in the Veracode Platform, if this URL scan is  linked to an application.    # noqa: E501

        :return: The linked_platform_app_name of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._linked_platform_app_name

    @linked_platform_app_name.setter
    def linked_platform_app_name(self, linked_platform_app_name):
        """Sets the linked_platform_app_name of this DetailedScan.

        Name of the linked application in the application portfoliio in the Veracode Platform, if this URL scan is  linked to an application.    # noqa: E501

        :param linked_platform_app_name: The linked_platform_app_name of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._linked_platform_app_name = linked_platform_app_name

    @property
    def scan_contact_info(self):
        """Gets the scan_contact_info of this DetailedScan.  # noqa: E501

        Contact information for the user to receive information about this URL scan.  # noqa: E501

        :return: The scan_contact_info of this DetailedScan.  # noqa: E501
        :rtype: ContactInformation
        """
        return self._scan_contact_info

    @scan_contact_info.setter
    def scan_contact_info(self, scan_contact_info):
        """Sets the scan_contact_info of this DetailedScan.

        Contact information for the user to receive information about this URL scan.  # noqa: E501

        :param scan_contact_info: The scan_contact_info of this DetailedScan.  # noqa: E501
        :type: ContactInformation
        """

        self._scan_contact_info = scan_contact_info

    @property
    def scan_locked(self):
        """Gets the scan_locked of this DetailedScan.  # noqa: E501

        If true, the URL scan is locked by Veracode and can only be edited or resubmitted by Veracode.  # noqa: E501

        :return: The scan_locked of this DetailedScan.  # noqa: E501
        :rtype: bool
        """
        return self._scan_locked

    @scan_locked.setter
    def scan_locked(self, scan_locked):
        """Sets the scan_locked of this DetailedScan.

        If true, the URL scan is locked by Veracode and can only be edited or resubmitted by Veracode.  # noqa: E501

        :param scan_locked: The scan_locked of this DetailedScan.  # noqa: E501
        :type: bool
        """

        self._scan_locked = scan_locked

    @property
    def scan_locked_on(self):
        """Gets the scan_locked_on of this DetailedScan.  # noqa: E501

        Date and time the URL scan was locked.  # noqa: E501

        :return: The scan_locked_on of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._scan_locked_on

    @scan_locked_on.setter
    def scan_locked_on(self, scan_locked_on):
        """Sets the scan_locked_on of this DetailedScan.

        Date and time the URL scan was locked.  # noqa: E501

        :param scan_locked_on: The scan_locked_on of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._scan_locked_on = scan_locked_on

    @property
    def created_on(self):
        """Gets the created_on of this DetailedScan.  # noqa: E501

        UTC-format date and time when the URL scan was created.  # noqa: E501

        :return: The created_on of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DetailedScan.

        UTC-format date and time when the URL scan was created.  # noqa: E501

        :param created_on: The created_on of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this DetailedScan.  # noqa: E501

        UTC-format date and time when the URL scan was last modified.  # noqa: E501

        :return: The last_modified_on of this DetailedScan.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this DetailedScan.

        UTC-format date and time when the URL scan was last modified.  # noqa: E501

        :param last_modified_on: The last_modified_on of this DetailedScan.  # noqa: E501
        :type: str
        """

        self._last_modified_on = last_modified_on

    @property
    def links(self):
        """Gets the links of this DetailedScan.  # noqa: E501


        :return: The links of this DetailedScan.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DetailedScan.


        :param links: The links of this DetailedScan.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def capabilities(self):
        """Gets the capabilities of this DetailedScan.  # noqa: E501


        :return: The capabilities of this DetailedScan.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this DetailedScan.


        :param capabilities: The capabilities of this DetailedScan.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

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
        if issubclass(DetailedScan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DetailedScan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other