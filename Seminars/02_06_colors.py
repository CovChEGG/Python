def colors(color):
    colors_dict = \
        {
            'r': 'red', 'red': 'r', 'к': 'r', 'красный': 'r',
            'b': 'blue', 'blue': 'b', 'c': 'b', 'синий': 'b',
            'y': 'yellow', 'yellow': 'y', 'ж': 'y', 'желтый': 'y', 'жёлтый': 'y',
            'p': 'purple', 'rb': 'purple', 'br': 'purple',
            'purple': 'p', 'ф': 'p', 'фиолетовый': 'p',
            'o': 'orange', 'ry': 'orange', 'yr': 'orange',
            'orange': 'o', 'о': 'o', 'оранжевый': 'o',
            'g': 'green', 'by': 'green', 'yb': 'green',
            'green': 'g', 'з': 'g', 'зеленый': 'g'
        }
    if color in colors_dict:
        return colors_dict[color]
    return None


def str_input_color(txt):
    while True:
        in_string = input(txt + ': ').lower().strip()
        color_typed  = colors(in_string)
        main_colors = ['r', 'y', 'b']
        if color_typed:
            if in_string in main_colors:
                return in_string
            elif color_typed in main_colors:
                return color_typed
            else:
                print('!!! Entered wrong color!!!')
        else:
            print('!!! Wrong input !!!')
        print('Choose one from: (R)ed, (G)reen, (B)lue')


print('Input two main colors to mix it')
print('(R)ed, (G)reen, (B)lue')
color1 = str_input_color('Input first color')
color2 = str_input_color('Input second color')
print(f'{colors(color1)} + {colors(color2)} = {colors(color1+color2)}')

