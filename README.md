# montagu-vault-py
A Python wrapper around [mrc-ide-vault](https://github.com/mrc-ide/mrc-ide-vault)

*NOTE: this is a legacy module from when we had a separate vimc vault, and should not be used for new work*

Use like so:

1. Add the submodule at some local path, let's say `vault`
   ```
   git submodule add https://github.com/vimc/montagu-vault-py vault
   ```
2. Add to your build/whatever script:
   ```
   pip3 install -r vault/requirements.txt
   ```
3. Import and use:
   ```
   from vault.vault import VaultClient

   vault = VaultClient()
   secret = vault.read_secret("secret/some/path")
   ```

# Interactive / non-interactive
`VaultClient` takes an optional argument `interactive`, which defaults
to `True`. If true, then if
[the github token](https://github.com/mrc-ide/mrc-ide-vault#authenticating-against-the-vault)
is missing from the current environment, the user will be interactively
prompted to enter their's. If it is false, a `MissingVaultToken`
exception will be thrown.
