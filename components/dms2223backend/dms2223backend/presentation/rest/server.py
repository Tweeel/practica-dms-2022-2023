""" REST API controllers responsible of handling the server operations.
"""

from typing import Tuple, Optional
from http import HTTPStatus


def health_test() -> Tuple[None, Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return (None, HTTPStatus.NO_CONTENT.value)
