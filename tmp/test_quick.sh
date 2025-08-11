#!/bin/bash

# Quick one-liner test with Python 3.11
docker run --rm python:3.11-slim bash -c 'pip install -q --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ markdown-to-slack-mkdown && python -c "from markdown_to_slack_mkdown import slack_convert; print(slack_convert(\"**Hello** [World](https://example.com) #123\"))"'