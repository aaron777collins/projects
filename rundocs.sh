#!/bin/bash
mkdocs build
python -m http.server 8080 --bind 127.0.0.1 --directory site
