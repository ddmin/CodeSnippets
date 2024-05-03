# KeePassXC

## Use OS keyring to unlock on login

```console
# store a new password:
secret-tool store --label='Keepass' <ATTRIBUTE> <DATABASE>.xdbx

# query and start keepassxc:
secret-tool lookup <ATTRIBUTE> <DATABASE>.xdbx | keepassxc --pw-stdin <DATABASE>.xdbx --keyfile <KEYFILE>
```

### if using KeePassXC appimage
- [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher)
