from GoogleAPICredentials import GoogleAPICredentials
import unittest


class GoogleAPICredentialsTest(unittest.TestCase):

  CREDENTIALS_PATH = "test/path/credentials.json"
  TOKEN_PATH = "test/path/token.json"

  def test_get_credentials_path(self):
    creds = GoogleAPICredentials(self.CREDENTIALS_PATH, self.TOKEN_PATH)
    self.assertEqual(creds.get_credentials_path(), self.CREDENTIALS_PATH, msg = "Incorrect credentials path")

  def test_get_token_path(self):
    creds = GoogleAPICredentials(self.CREDENTIALS_PATH, self.TOKEN_PATH)
    self.assertEqual(creds.get_token_path(), self.TOKEN_PATH, msg = "Incorrect token path")


if (__name__ == "__main__"):
  unittest.main()
