from main import string_to_morse


def test_string_to_morse():
    assert string_to_morse('E') == '.'
    assert string_to_morse('3') == '...--'
    assert string_to_morse("!?@#$%^&*()") == ''
    assert string_to_morse("HELLO") == '.... . .-.. .-.. ---'
    assert string_to_morse("123") == '.---- ..--- ...--'
    assert string_to_morse("HeLlO") == '.... . .-.. .-.. ---'
    assert string_to_morse("Python") == '.--. -.-- - .... --- -.'
