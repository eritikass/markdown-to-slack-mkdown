#!/bin/bash

# Test the package from Test PyPI using Docker

echo "Testing markdown-to-slack-mkdown from Test PyPI..."
echo "================================================"

# Test with different Python versions
for PYTHON_VERSION in 3.12 3.13; do
    echo ""
    echo "Testing with Python $PYTHON_VERSION..."
    echo "-----------------------------------"
    
    docker run --rm python:$PYTHON_VERSION-slim bash -c '
        # Install from Test PyPI
        pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ markdown-to-slack-mkdown
        
        # Test import and basic usage
        python -c "
from markdown_to_slack_mkdown import slack_convert, SlackConvertOptions

# Test basic conversion
result = slack_convert(\"**bold** and [link](https://example.com)\")
print(f\"Basic test: {result}\")
assert result == \"*bold* and <https://example.com|link>\"

# Test with options
options = SlackConvertOptions(
    repo_name=\"owner/repo\",
    headlines=True
)
result = slack_convert(\"## Header\\n#123\", options)
print(f\"Options test: {result}\")
assert \"*Header*\" in result

print(\"✅ All tests passed for Python '$PYTHON_VERSION'!\")
"
    '
done

echo ""
echo "================================================"
echo "✅ Package testing complete!"
