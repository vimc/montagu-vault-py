# montagu-vault-py
A Python wrapper around [montagu-vault](https://github.com/vimc/montagu-vault)

Use like so:

1. Add the submodule:
   ```
   git submodule add https://github.com/vimc/montagu-vault-py <PATH>
   ```
2. Add to your build/whatever script:
   ```
   pip3 install -r <PATH>/requirements.txt
   ```
3. Import and use:
   ```
   from PATH import VaultClient

   vault = VaultClient()
   secret = vault.read_secret("secret/some/path")
   ```

# Interactive / non-interactive
`VaultClient` takes an optional argument `interactive`, which defaults
to `True`. If true, then if
[the github token](https://github.com/vimc/montagu-vault#authenticating-against-the-vault)
is missing from the current environment, the user will be interactively
prompted to enter their's. If it is false, a `MissingVaultToken`
exception will be thrown.
