""" REST API controllers responsible of handling the security schemas.
"""

from typing import Dict
from flask import current_app
import requests
from connexion.exceptions import Unauthorized  # type: ignore
from dms2223backend.data.config import BackendConfiguration


def verify_api_key(token: str) -> Dict:
    """Callback testing the received API key.

    Args:
        - token (str): The received API key.

    Raises:
        - Unauthorized: When the given API key is not valid.

    Returns:
        - Dict: Information retrieved from the key to be passed to the endpoints.
    """
    with current_app.app_context():
        cfg: BackendConfiguration = current_app.cfg
        if not token in cfg.get_authorized_api_keys():
            raise Unauthorized('Invalid API key')
    return {}


def verify_token(token: str) -> bool:
    """Callback testing a JWS user token.

    Args:
        - token (str): The JWS user token received.

    Raises:
        - Unauthorized: When the token is incorrect.

    Returns:
        - Dict: A dictionary with the user name (key `user`) if the credentials are correct.
    """

    with current_app.app_context():
        cfg = current_app.cfg.get_auth_service()
        base_url = f"http://{cfg['host']}:{cfg['port']}/api/v1"
        current_app.logger.warn(base_url)
        current_app.logger.warn(token)
        response: requests.Response = requests.get(
            base_url + '/auth',
            headers={
                'Authorization': f'Bearer {token}',
                'X-ApiKey-Auth': cfg['apikey_secret']
            },
            timeout=60
        )

        if not response.ok:
            raise Unauthorized('Invalid token')

    return True
