# Qlik JWT Token generator

This script was created to generate JWT tokens to authenticate the qlik-cli
tool to Qlik Sense Enterprise. See the [qlik-cli documentation][qlik-cli-docs]
for why you might want to do this.

The script might be adaptable to create JWT tokens for other purposes, but this
is not the primary goal.

## Install

This script is setup as a Python package. You should be able to install it
directly with `pip` or `pipx`:

``` sh
pip install qlikjwt@git+https://github.com/swsphn/qlikjwt.git
```

OR

``` sh
pipx install qlikjwt@git+https://github.com/swsphn/qlikjwt.git
```

This will install `qlikjwt` as an importable Python library and an executable
cli tool. (Or just an executable tool in the case of `pipx`)

## Usage

Run the following to view the built-in help:

``` sh
qlikjwt --help

Usage: qlikjwt [OPTIONS] JWT_PRIVATE_KEY

  Generate a JWT token from a private key and a payload. Payload options may
  be specified using optional arguments. If not specified, the user will be
  prompted to enter payload values.

Arguments:
  JWT_PRIVATE_KEY  Path to JWT private key  [required]

Options:
  --name TEXT               Token owner's name
  --user TEXT               User ID
  --directory TEXT          User directory
  --email TEXT              Email address
  --jwt-audience TEXT       JWT Intended Audience (aud)
  --group TEXT              Access group. Repeat this option to specify
                            multiple groups.
  --days-to-expiry INTEGER  Days until JWT token expires
  --help                    Show this message and exit.
```


[qlik-cli-docs]: https://qlik.dev/manage/automate/qlik-cli-qrs-get-started/#configure-a-context-in-qlik-cli
