#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
#here = os.path.abspath(os.path.dirname(__file__))
here = os.path.abspath(os.path.dirname("/Users/mzod/coding/certs/cisco/devnet-associate-200-901/dnav3-code/intro-python/parsing-json/"))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    # Read in the json text (which is a "class str")
    json_text = file.read()
    # Parse the json string into native python data (which is a "class dict")
    json_data = json.loads(json_text)


# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    print("{name}: {ip} {netmask}".format(
        name=interface["name"],
        ip=interface["ietf-ip:ipv4"]["address"][0]["ip"],
        netmask=interface["ietf-ip:ipv4"]["address"][0]["netmask"],
        ))
