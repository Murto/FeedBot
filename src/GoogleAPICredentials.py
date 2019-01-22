from typing import NoReturn


class GoogleAPICredentials:

  def __init__(self, credentials_path : str, token_path : str) -> NoReturn:
    self.credentials_path = credentials_path
    self.token_path = token_path

  def get_credentials_path(self) -> str:
    return self.credentials_path

  def get_token_path(self) -> str:
    return self.token_path
