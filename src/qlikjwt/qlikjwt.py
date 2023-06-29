from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional

import jwt
import typer
from typing_extensions import Annotated


def get_jwt_payload(
    name: str = None,
    user: str = None,
    directory: str = None,
    email: str = None,
    jwt_audience: str = None,
    groups: List[str] = None,
    days_to_expiry: int = None,
):
    """Create a JWT payload.

    If keyword arguments are missing, promp the user to enter the
    required value.

    Keyword Arguments:
        name: str            JWT token owner's name
        user: str            Username
        directory: str       AD directory
        email: str           Email address
        jwt_audience: str    JWT Intended Audience (aud)
        groups: List[str]    List of access groups
        days_to_expiry: int  Number of days until token expires
    """
    payload = {}

    if not all((name, user, directory, email, jwt_audience, groups, days_to_expiry)):
        print("Enter the jwt payload values:")

    payload["name"] = name or input("Name: ")
    payload["user"] = user or input("Username: ")
    payload["directory"] = directory or input("AD directory: ")
    payload["email"] = email or input("Email address: ")
    payload["aud"] = jwt_audience or input("JWT Intended Audience: ")

    if not groups:
        groups = []
        group = None
        group = input("Enter access groups (blank to finish): ")
        while group:
            groups.append(group)
            group = input("Enter access groups (blank to finish): ")

    payload["groups"] = groups

    days_to_expiry = days_to_expiry or int(input("Days until the token expires: "))
    expiry_date = datetime.now(tz=timezone.utc) + timedelta(days=days_to_expiry)
    payload["exp"] = expiry_date

    return payload


def main(
    jwt_private_key: Annotated[Path, typer.Argument(help="Path to JWT private key")],
    name: Annotated[
        str, typer.Option(help="Token owner's name", show_default=False)
    ] = "",
    user: Annotated[str, typer.Option(help="User ID", show_default=False)] = "",
    directory: Annotated[
        str, typer.Option(help="User directory", show_default=False)
    ] = "",
    email: Annotated[str, typer.Option(help="Email address", show_default=False)] = "",
    jwt_audience: Annotated[
        str, typer.Option(help="JWT Intended Audience (aud)", show_default=False)
    ] = "",
    groups: Annotated[
        Optional[List[str]],
        typer.Option(
            "--group",
            help="Access group. Repeat this option to specify multiple groups.",
            show_default=False,
        ),
    ] = None,
    days_to_expiry: Annotated[
        int, typer.Option(help="Days until JWT token expires", show_default=False)
    ] = 0,
):
    """Generate a JWT token from a private key and a payload.
    Payload options may be specified using optional arguments.
    If not specified, the user will be prompted to enter payload values.
    """

    with open(jwt_private_key) as file:
        privatekey = file.read()

    payload = get_jwt_payload(
        name=name,
        user=user,
        directory=directory,
        email=email,
        jwt_audience=jwt_audience,
        groups=groups,
        days_to_expiry=days_to_expiry,
    )

    print(f"\nToken expires: {payload['exp']}.")

    token = jwt.encode(payload, privatekey, algorithm="RS256")
    print("JWT token (keep secret!):\n")
    print(token)
    print()


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
