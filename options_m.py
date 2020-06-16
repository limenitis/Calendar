class Options():
    
    def new_event(self):
        print('new_event work')
        
    def new_task(self):
        print('new_task work')
        
    def change_layoyt_calendar(self):
        print('change_layoyt_calendar work')

    def change_layoyt_tasks(self):
        print('change_layoyt_tasks work')

    def delete_task(self):
        print('delete_task work')

    def update_task(self):
        print('update_task work')


def convert_str_to_int(string):
    r = ''
    g = ''
    b = ''
    invis = ''

    switch = 0

    for symbol in string:
        if (symbol != ','):
            if symbol == ' ':
                continue

            elif switch == 0:
                r = r + symbol

            elif switch == 1:
                g = g + symbol

            elif switch == 2:
                b = b + symbol

            elif  switch == 3:
                invis = invis + symbol
        
        elif(symbol == ','):
            switch += 1

    r = int(r)
    g = int(g)
    b = int(b)
    
    if invis != '':
        invis = float(invis)
    else:
        invis = 1

    return r, g, b, invis

def rgb(r = None, g = None, b = None, invis = 1):

    if (type(r) == str):
       r, g, b, invis = convert_str_to_int(r)

    return (r/255,g/255,b/255,invis)
