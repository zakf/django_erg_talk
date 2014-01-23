# format_text.py

def center_text(text, width=80, cap='#', fill='=', inner_cap='', out='print'):
    """Make a title centered inside filler characters
    
    Arguments:
        
        text        String, this appears in the center
        
        width       Integer, number of characters wide
        
        cap         String, this appears as the "bookends" at either end of 
                    the output line. Here are some values:
                    ' '
                    '#'
                    '+'
                    '//'
                    '/*'    NOTE: If you use this, it will be reversed on the 
                            right cap such that it closes the comment.
        
        fill        String, this appears repeatedly to create the visual 
                    demarcation. Here are some values:
                    ' '
                    '='
                    '-'
                    '#'
        
        inner_cap   String, this appears just inside the cap and just outside 
                    of the fill. Here are some values:
                    ''      Empty string, no inner_cap
                    ' '
                    '   '   Three spaces
        
        out         String, either 'print' or 'return'. How would you like 
                    the output delivered?
    
    """
    
    len_text = len(text)
    len_cap = len(cap)
    len_inner_cap = len(inner_cap)
    
    len_fill = width - (2 * (len_cap + len_inner_cap) + 2) - len_text
    
    if len_fill < 0:
        raise Exception("The input text is too wide for the width, cap, and "
                        "inner_cap that you have chosen. len_fill = %s." % 
                        len_fill)
    
    len_fill_left = len_fill // 2
    len_fill_right = len_fill_left + (len_fill % 2)
    
    fill_left = make_fill(fill, len_fill_left)
    fill_right = make_fill(fill, len_fill_right)
    
    output = [
        cap,
        inner_cap,
        fill_left,
        ' ',
        text,
        ' ',
        fill_right,
        inner_cap,
    ]
    
    if cap == '/*':
        output.append('*/')
    else:
        output.append(cap)
    
    output_str = ''.join(output)
    if out == 'print':
        print output_str
    else:
        return output_str


def make_fill(fill, length):
    """Repeat 'fill' as many times as necessary, then trim to 'length'
    
    Arguments:
        
        fill        String, e.g. '=', '-', '- ', '*'
        
        length      Integer, the length of the desired output string
    
    """
    
    num_repeats = length // len(fill)
    remainder = length % len(fill)
    if remainder:
        num_repeats += 1
    
    output = fill * num_repeats
    return output[:length]


def d(text, width=80, cap='#', fill='=', inner_cap='', out='print'):
    """Double-line, looks like this:
    
    #================================ Text ================================#
    
    """
    
    return center_text(text, width, cap, fill, inner_cap, out)


def s(text, width=80, cap='#', fill='-', inner_cap='', out='print'):
    """Single-line, looks like this:
    
    #-------------------------------- Text --------------------------------#
    
    """
    
    return center_text(text, width, cap, fill, inner_cap, out)


def help():
    print center_text.__doc__
