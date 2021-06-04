import json

from requests import Response

class MeiliSearchError(Exception):
    """Generic class for MeiliSearch error handling"""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'MeiliSearchError. Error message: {self.message}.'

class MeiliSearchApiError(MeiliSearchError):
    """Error sent by MeiliSearch API"""

    def __init__(self, error: str, request: Response) -> None:
        self.status_code = request.status_code
        if request.text:
            self.message = f'{json.loads(request.text)["message"]}'
            self.error_code = f'{json.loads(request.text)["errorCode"]}'
            self.error_link = f'{json.loads(request.text)["errorLink"]}'
        else:
            self.message = error
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'MeiliSearchApiError. Error code: {self.error_code}. Error message: {self.message}. Error documentation: {self.error_link}'

class MeiliSearchCommunicationError(MeiliSearchError):
    """Error when connecting to MeiliSearch"""

    def __str__(self) -> str:
        return f'MeiliSearchCommunicationError, {self.message}'

class MeiliSearchTimeoutError(MeiliSearchError):
    """Error when MeiliSearch operation takes longer than expected"""

    def __str__(self) -> str:
        return f'MeiliSearchTimeoutError, {self.message}'
