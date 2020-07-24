# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CallEngineModifyConferenceRequest(object):

    """Implementation of the 'CallEngineModifyConferenceRequest' model.

    TODO: type model description here.

    Attributes:
        status (StatusEnum): TODO: type description here.
        redirect_url (string): TODO: type description here.
        redirect_method (RedirectMethodEnum): TODO: type description here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_url": 'redirectUrl',
        "status": 'status',
        "redirect_method": 'redirectMethod',
        "username": 'username',
        "password": 'password'
    }

    def __init__(self,
                 redirect_url=None,
                 status=None,
                 redirect_method=None,
                 username=None,
                 password=None):
        """Constructor for the CallEngineModifyConferenceRequest class"""

        # Initialize members of the class
        self.status = status
        self.redirect_url = redirect_url
        self.redirect_method = redirect_method
        self.username = username
        self.password = password

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        redirect_url = dictionary.get('redirectUrl')
        status = dictionary.get('status')
        redirect_method = dictionary.get('redirectMethod')
        username = dictionary.get('username')
        password = dictionary.get('password')

        # Return an object of this model
        return cls(redirect_url,
                   status,
                   redirect_method,
                   username,
                   password)
