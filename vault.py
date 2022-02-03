from getpass import getpass

import os

import hvac

from .exceptions import MissingVaultToken

DEFAULT_VAULT_ADDR = "https://support.montagu.dide.ic.ac.uk:8200"


class VaultClient(object):
    """A simple wrapper around hvac for use with montagu-vault

    Args:
        interactive (bool): If the environment does not contain the vault
        token and this is True, the user will be interactively prompted for
        their token. If it is False, an exception will be thrown instead.
    """

    def __init__(self, interactive=True):
        self.client = None
        self.interactive = interactive

    def _connect(self):
        vault_url = os.environ.get("VAULT_ADDR", DEFAULT_VAULT_ADDR)
        vault_token = self._get_token()
        self.client = hvac.Client(url=vault_url)
        self.client.auth.github.login(token=vault_token)

    def _get_token(self):
        vault_token = os.environ.get("VAULT_AUTH_GITHUB_TOKEN")
        if not vault_token:
            if self.interactive:
                prompt = "Please paste your vault GitHub access token: "
                vault_token = getpass(prompt).strip()
            else:
                raise MissingVaultToken()
        return vault_token

    def read_secret(self, path, field='value'):
        if not self.client:
            self._connect()
        secret = self.client.read(path)
        return secret['data'][field]
