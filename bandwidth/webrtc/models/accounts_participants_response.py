# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from bandwidth.webrtc.models.participant import Participant


class AccountsParticipantsResponse(object):

    """Implementation of the 'Accounts Participants Response' model.

    TODO: type model description here.

    Attributes:
        participant (Participant): A participant object
        token (string): Auth token for the returned participant  This should
            be passed to the participant so that they can connect to the
            platform

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "participant": 'participant',
        "token": 'token'
    }

    def __init__(self,
                 participant=None,
                 token=None):
        """Constructor for the AccountsParticipantsResponse class"""

        # Initialize members of the class
        self.participant = participant
        self.token = token

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
        participant = Participant.from_dictionary(dictionary.get('participant')) if dictionary.get('participant') else None
        token = dictionary.get('token')

        # Return an object of this model
        return cls(participant,
                   token)
