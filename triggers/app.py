import json
import datetime
import time
import random

from triggers import custom_auth
from triggers import custom_message
from triggers import post_auth
from triggers import post_confirmation
from triggers import pre_auth
from triggers import pre_signup
from triggers import token_generation
from triggers import user_migration

PRE_SIGNUP = [
    "PreSignUp_SignUp",
    "PreSignUp_AdminCreateUser"
]

POST_CONFIRMATION = [
    "PostConfirmation_ConfirmSignUp",
    "PostConfirmation_ConfirmForgotPassword"
]

PRE_AUTH = [
    "PreAuthentication_Authentication"
]

POST_AUTH = [
    "PostAuthentication_Authentication"
]

CUSTOM_AUTH = [
    "DefineAuthChallenge_Authentication",
    "CreateAuthChallenge_Authentication",
    "VerifyAuthChallengeResponse_Authentication"
]


TOKEN_GENERATION = [
    "TokenGeneration_HostedAuth",
    "TokenGeneration_Authentication",
    "TokenGeneration_NewPasswordChallenge",
    "TokenGeneration_AuthenticateDevice",
    "TokenGeneration_RefreshTokens"
]

USER_MIGRATION = [
    "UserMigration_Authentication",
    "UserMigration_ForgotPassword"
]

CUSTOM_MESSAGE = [
    "CustomMessage_SignUp",
    "CustomMessage_AdminCreateUser",
    "CustomMessage_ResendCode",
    "CustomMessage_ForgotPassword",
    "CustomMessage_UpdateUserAttribute",
    "CustomMessage_VerifyUserAttribute",
    "CustomMessage_Authentication"
]


def lambda_handler(event, context):
    print(json.dumps(event))

    if event.triggerSource in PRE_SIGNUP:
        pre_signup(event,context)
    elif event.triggerSource in POST_CONFIRMATION:
        post_confirmation(event, context)

    return event


