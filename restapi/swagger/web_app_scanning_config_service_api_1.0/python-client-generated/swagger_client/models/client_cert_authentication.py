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


class ClientCertAuthentication(object):
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
        'authtype': 'str',
        'authentication_id': 'str',
        'password': 'str',
        'cert': 'str'
    }

    attribute_map = {
        'authtype': 'authtype',
        'authentication_id': 'authentication_id',
        'password': 'password',
        'cert': 'cert'
    }

    def __init__(self, authtype=None, authentication_id=None, password=None, cert=None):  # noqa: E501
        """ClientCertAuthentication - a model defined in Swagger"""  # noqa: E501

        self._authtype = None
        self._authentication_id = None
        self._password = None
        self._cert = None
        self.discriminator = None

        if authtype is not None:
            self.authtype = authtype
        if authentication_id is not None:
            self.authentication_id = authentication_id
        if password is not None:
            self.password = password
        if cert is not None:
            self.cert = cert

    @property
    def authtype(self):
        """Gets the authtype of this ClientCertAuthentication.  # noqa: E501

        The type of authentication. Only the value CERT is expected.  # noqa: E501

        :return: The authtype of this ClientCertAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._authtype

    @authtype.setter
    def authtype(self, authtype):
        """Sets the authtype of this ClientCertAuthentication.

        The type of authentication. Only the value CERT is expected.  # noqa: E501

        :param authtype: The authtype of this ClientCertAuthentication.  # noqa: E501
        :type: str
        """

        self._authtype = authtype

    @property
    def authentication_id(self):
        """Gets the authentication_id of this ClientCertAuthentication.  # noqa: E501

        Unique record identifier.  # noqa: E501

        :return: The authentication_id of this ClientCertAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._authentication_id

    @authentication_id.setter
    def authentication_id(self, authentication_id):
        """Sets the authentication_id of this ClientCertAuthentication.

        Unique record identifier.  # noqa: E501

        :param authentication_id: The authentication_id of this ClientCertAuthentication.  # noqa: E501
        :type: str
        """

        self._authentication_id = authentication_id

    @property
    def password(self):
        """Gets the password of this ClientCertAuthentication.  # noqa: E501

        The password to use.  # noqa: E501

        :return: The password of this ClientCertAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ClientCertAuthentication.

        The password to use.  # noqa: E501

        :param password: The password of this ClientCertAuthentication.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def cert(self):
        """Gets the cert of this ClientCertAuthentication.  # noqa: E501

        The encoded, base64 certificate.  # noqa: E501

        :return: The cert of this ClientCertAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this ClientCertAuthentication.

        The encoded, base64 certificate.  # noqa: E501

        :param cert: The cert of this ClientCertAuthentication.  # noqa: E501
        :type: str
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
        if issubclass(ClientCertAuthentication, dict):
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
        if not isinstance(other, ClientCertAuthentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
