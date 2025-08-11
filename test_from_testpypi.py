#!/usr/bin/env python3
"""
Test the package after installing from Test PyPI.

First install the package:
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ markdown-to-slack-mkdown

Then run this script:
python test_from_testpypi.py
"""


def test_package():
    try:
        from markdown_to_slack_mkdown import slack_convert, SlackConvertOptions

        print("✅ Package imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import package: {e}")
        print("\nInstall with:")
        print(
            "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ markdown-to-slack-mkdown"
        )
        return False

    # Test cases
    tests = [
        ("**bold**", "*bold*"),
        ("~~strike~~", "~strike~"),
        ("[link](https://example.com)", "<https://example.com|link>"),
        ("@username", "<https://github.com/username|@username>"),
        ("* item", "• item"),
    ]

    print("\nRunning tests...")
    for input_text, expected in tests:
        result = slack_convert(input_text)
        if result == expected:
            print(f"✅ '{input_text}' -> '{result}'")
        else:
            print(f"❌ '{input_text}' -> Expected: '{expected}', Got: '{result}'")
            return False

    # Test with options
    options = SlackConvertOptions(repo_name="owner/repo", headlines=True)

    test_input = "## Header\nFix #123"
    result = slack_convert(test_input, options)

    if "*Header*" in result and "owner/repo" in result:
        print(f"✅ Options test passed")
    else:
        print(f"❌ Options test failed: {result}")
        return False

    print("\n🎉 All tests passed!")
    return True


if __name__ == "__main__":
    import sys

    sys.exit(0 if test_package() else 1)
