class MissingVaultToken(Exception):
    def __init__(self):
        message = "Missing vault token. Please export VAULT_AUTH_GITHUB_TOKEN"
        super().__init__(message)
