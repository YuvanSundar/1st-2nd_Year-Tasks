import re


def is_valid_ethereum_address(address):
    eth_address_pattern = re.compile(r'^0x[0-9a-fA-F]{40}$')

    
    if eth_address_pattern.match(address):
        return True
    else:
        return False


test_address = "0x731bFF30E7A4d2ECeF5F15F6E48BfB8363E3FaA3"


if is_valid_ethereum_address(test_address):
    print("true")
else:
    print("false")