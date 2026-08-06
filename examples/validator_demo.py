"""
OpenLSP Validator Demo

Demonstrates message validation.
"""

from openlsp_core.message import create_message
from openlsp_core.validator import validate_message


def main():

    message = create_message(
        "client",
        "server",
        "Hello OpenLSP!"
    )

    print("Created message:")
    print(message)

    print()

    print("Validation result:")

    if validate_message(message):
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
