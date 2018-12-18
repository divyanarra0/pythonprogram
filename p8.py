def snake11_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake11_to_camel('aab _xxy')),
