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


class AnalysisRequest(object):
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
        'name': 'str',
        'org_info': 'OrgInformation',
        'scan_setting': 'ScanSetting',
        'scans': 'list[ScanRequest]',
        'schedule': 'ScanSchedule',
        'special_instructions': 'str',
        'visibility': 'VisibilitySetup'
    }

    attribute_map = {
        'name': 'name',
        'org_info': 'org_info',
        'scan_setting': 'scan_setting',
        'scans': 'scans',
        'schedule': 'schedule',
        'special_instructions': 'special_instructions',
        'visibility': 'visibility'
    }

    def __init__(self, name=None, org_info=None, scan_setting=None, scans=None, schedule=None, special_instructions=None, visibility=None):  # noqa: E501
        """AnalysisRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._org_info = None
        self._scan_setting = None
        self._scans = None
        self._schedule = None
        self._special_instructions = None
        self._visibility = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if org_info is not None:
            self.org_info = org_info
        if scan_setting is not None:
            self.scan_setting = scan_setting
        if scans is not None:
            self.scans = scans
        if schedule is not None:
            self.schedule = schedule
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if visibility is not None:
            self.visibility = visibility

    @property
    def name(self):
        """Gets the name of this AnalysisRequest.  # noqa: E501

        Name of the Dynamic Analysis. The name must be unique to the application porfolio of the organization and the  length must be between 6 and 256 characters.   # noqa: E501

        :return: The name of this AnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisRequest.

        Name of the Dynamic Analysis. The name must be unique to the application porfolio of the organization and the  length must be between 6 and 256 characters.   # noqa: E501

        :param name: The name of this AnalysisRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_info(self):
        """Gets the org_info of this AnalysisRequest.  # noqa: E501

        Organization information.  # noqa: E501

        :return: The org_info of this AnalysisRequest.  # noqa: E501
        :rtype: OrgInformation
        """
        return self._org_info

    @org_info.setter
    def org_info(self, org_info):
        """Sets the org_info of this AnalysisRequest.

        Organization information.  # noqa: E501

        :param org_info: The org_info of this AnalysisRequest.  # noqa: E501
        :type: OrgInformation
        """

        self._org_info = org_info

    @property
    def scan_setting(self):
        """Gets the scan_setting of this AnalysisRequest.  # noqa: E501

        The Dynamic Analysis scan level setting that applies to all URL scans in this analysis.  # noqa: E501

        :return: The scan_setting of this AnalysisRequest.  # noqa: E501
        :rtype: ScanSetting
        """
        return self._scan_setting

    @scan_setting.setter
    def scan_setting(self, scan_setting):
        """Sets the scan_setting of this AnalysisRequest.

        The Dynamic Analysis scan level setting that applies to all URL scans in this analysis.  # noqa: E501

        :param scan_setting: The scan_setting of this AnalysisRequest.  # noqa: E501
        :type: ScanSetting
        """

        self._scan_setting = scan_setting

    @property
    def scans(self):
        """Gets the scans of this AnalysisRequest.  # noqa: E501

        The list of URL scans included in the analysis.  # noqa: E501

        :return: The scans of this AnalysisRequest.  # noqa: E501
        :rtype: list[ScanRequest]
        """
        return self._scans

    @scans.setter
    def scans(self, scans):
        """Sets the scans of this AnalysisRequest.

        The list of URL scans included in the analysis.  # noqa: E501

        :param scans: The scans of this AnalysisRequest.  # noqa: E501
        :type: list[ScanRequest]
        """

        self._scans = scans

    @property
    def schedule(self):
        """Gets the schedule of this AnalysisRequest.  # noqa: E501

        The schedule for the URL scan. This is optional. If not specified, no URL scans will run. You can still run verification scans.   # noqa: E501

        :return: The schedule of this AnalysisRequest.  # noqa: E501
        :rtype: ScanSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AnalysisRequest.

        The schedule for the URL scan. This is optional. If not specified, no URL scans will run. You can still run verification scans.   # noqa: E501

        :param schedule: The schedule of this AnalysisRequest.  # noqa: E501
        :type: ScanSchedule
        """

        self._schedule = schedule

    @property
    def special_instructions(self):
        """Gets the special_instructions of this AnalysisRequest.  # noqa: E501

        Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis.  # noqa: E501

        :return: The special_instructions of this AnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this AnalysisRequest.

        Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis.  # noqa: E501

        :param special_instructions: The special_instructions of this AnalysisRequest.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def visibility(self):
        """Gets the visibility of this AnalysisRequest.  # noqa: E501

        Visibility setup.  # noqa: E501

        :return: The visibility of this AnalysisRequest.  # noqa: E501
        :rtype: VisibilitySetup
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this AnalysisRequest.

        Visibility setup.  # noqa: E501

        :param visibility: The visibility of this AnalysisRequest.  # noqa: E501
        :type: VisibilitySetup
        """

        self._visibility = visibility

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
        if issubclass(AnalysisRequest, dict):
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
        if not isinstance(other, AnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
