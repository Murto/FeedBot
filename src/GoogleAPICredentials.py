from typing import NoReturn


class GoogleAPICredentials:

  def __init__(self, credentialsJSONPath : str, tokenPath : str) -> NoReturn:
    self.credentialsJSONPath = credentialsJSONPath
    self.tokenPath = tokenPath

  def getCredentialsJSONPath(self) -> str:
    return self.credentialsJSONPath

  def getTokenPath(self) -> str:
    return self.tokenPath
