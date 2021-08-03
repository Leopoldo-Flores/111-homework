#!/usr/bin/env python3
# -*- coding: utf8 -*-
#Simple flask app

from flask import Flask

app = Flask(__name__)

@app.route("/aboutme")
def about_me():
    me = {
        "first_name":":Leopoldo",
        "last_name":"Flores",
        "hobbies":"Play guitar and drums",
        "test": True

    }
    return me