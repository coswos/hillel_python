def hashtag(message, tag='#'):
    text = tag + message
    text = text.title()
    text = text.strip().replace(' ', '')
    if len(text) > 140:
        return False
    if message == '' or text == '': raise Exception('Error Bro ;)')
    if message == '\"' or text == '\"' or message == "\'" or text == "\'": raise Exception('Error Bro ;)')

    print(
        'get your hashtag', text,
    )


example_text = 'hello my friend '
hashtag(example_text)
