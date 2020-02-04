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


class AuthenticationConfigurationAuthentications(object):
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
        'auto': 'AutoAuthentication',
        'form': 'FormAuthentication',
        'basic': 'BasicAuthentication',
        'cert': 'ClientCertAuthentication'
    }

    attribute_map = {
        'auto': 'AUTO',
        'form': 'FORM',
        'basic': 'BASIC',
        'cert': 'CERT'
    }

    def __init__(self, auto=None, form=None, basic=None, cert=None):  # noqa: E501
        """AuthenticationConfigurationAuthentications - a model defined in Swagger"""  # noqa: E501

        self._auto = None
        self._form = None
        self._basic = None
        self._cert = None
        self.discriminator = None

        if auto is not None:
            self.auto = auto
        if form is not None:
            self.form = form
        if basic is not None:
            self.basic = basic
        if cert is not None:
            self.cert = cert

    @property
    def auto(self):
        """Gets the auto of this AuthenticationConfigurationAuthentications.  # noqa: E501

        Auto-login authentication.  # noqa: E501

        :return: The auto of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :rtype: AutoAuthentication
        """
        return self._auto

    @auto.setter
    def auto(self, auto):
        """Sets the auto of this AuthenticationConfigurationAuthentications.

        Auto-login authentication.  # noqa: E501

        :param auto: The auto of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :type: AutoAuthentication
        """

        self._auto = auto

    @property
    def form(self):
        """Gets the form of this AuthenticationConfigurationAuthentications.  # noqa: E501

        Form-based authentication.  # noqa: E501

        :return: The form of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :rtype: FormAuthentication
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this AuthenticationConfigurationAuthentications.

        Form-based authentication.  # noqa: E501

        :param form: The form of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :type: FormAuthentication
        """

        self._form = form

    @property
    def basic(self):
        """Gets the basic of this AuthenticationConfigurationAuthentications.  # noqa: E501

        Basic authentication.  # noqa: E501

        :return: The basic of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :rtype: BasicAuthentication
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this AuthenticationConfigurationAuthentications.

        Basic authentication.  # noqa: E501

        :param basic: The basic of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :type: BasicAuthentication
        """

        self._basic = basic

    @property
    def cert(self):
        """Gets the cert of this AuthenticationConfigurationAuthentications.  # noqa: E501

        Client certificate-based authentication.  # noqa: E501

        :return: The cert of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :rtype: ClientCertAuthentication
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this AuthenticationConfigurationAuthentications.

        Client certificate-based authentication.  # noqa: E501

        :param cert: The cert of this AuthenticationConfigurationAuthentications.  # noqa: E501
        :type: ClientCertAuthentication
        """

        self._cert = cert

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
        if issubclass(AuthenticationConfigurationAuthentications, dict):
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
        if not isinstance(other, AuthenticationConfigurationAuthentications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other