from datetime import datetime
import pyautogui as pag, pyperclip
import requests
import json
import time
import mylinks as myl

start_pause = 3
click_pause = 0.6
lastblock = ''
list_subsite = ['Свой блог', 'Скриншоты', 'Игры', 'Индустрия', 'Gamedev', 'Кино и сериалы', 'Мемы', 'Жизнь', 'Инди', 'Арт', 'Офтоп', 'Видео', 'Аниме', 'Вопросы', 'Виабу']
def start():
    try:
        links = link_inizialization()
        for link in links:
            parse_to_dtf(link)
    except KeyboardInterrupt:
        print('\nГотово!')
    
def parse_to_dtf(link):
    print('parse_to_dtf')
    headers = {
        'accept': 'application/json',
        'X-Device-Token' : '36f138d0fb097faaa995517ddf82d217806e0f6cc3283dcbbc11cf82a4bc305e'
    }
    params = (
        ('id', link),
        )
    response = requests.get('https://api.dtf.ru/v2.1/content', headers=headers, params=params)
    data = json.loads(response.text)
    title = data['result']['title']
    subsite = data['result']['subsite']['name']
    author = data['result']['author']['name']
    date = data['result']['date']
    blocks = data['result']['blocks']
    pag.FAILSAFE = False
    pag.PAUSE = 0
    time.sleep(start_pause)
    #goto_menu()
    #create_page()
    click(505, 705)
    for block in blocks:
        set_block(block)
        lastblock = block['type']
    scroll_up()
    set_date(date)
    set_author(author)
    set_subsite(subsite)
    set_title(title)

def goto_menu():
    click(121,1054)
    time.sleep(click_pause*2)
    
def create_page():
    print('create_page')
    pag.scroll(-5000)
    time.sleep(click_pause)
    click(608,924)
    time.sleep(click_pause)
    
def set_title(title):
    print('set_title')
    pyperclip.copy(title)
    click(922,475)
    time.sleep(click_pause)
    ctrl_v()
    
def set_author(author):
    print('set_author')
    pyperclip.copy(author)
    pag.click(x=800, y=620, clicks=4, interval=0.2)
    time.sleep(click_pause)
    ctrl_v()
    time.sleep(click_pause)
    
def set_subsite(subsite):
    print('set_subsite')
    click(800,585)
    time.sleep(click_pause)
    click(840,651)
    time.sleep(click_pause)
    click(1320,625)
    time.sleep(click_pause)
    find_subsite(subsite)
    ctrl_v()
    click(1300,695) 
    time.sleep(click_pause)
    
def set_date(date):
    print('set_date')
    date = datetime.utcfromtimestamp(date).strftime('%d-%m-%Y')
    pyperclip.copy(date)
    pag.click(x=800, y=650, clicks=4, interval=0.1)
    ctrl_v()
    time.sleep(click_pause)
    
def set_block(block):
    bt = block['type']
    data = block['data']
    change_to_default(bt)
    if bt == 'text':
        make_text(data)
    elif bt == 'header':
        make_header(data)
    #elif bt == 'media':
        #make_picture(data)
    elif bt == 'incut':
        make_incut(data)
    elif bt == 'list':
        make_list(data)
    elif bt == 'delimiter':
        make_delimiter(data)
    else:
        print('неизвестный элемент: '+bt)
    move_down()
    time.sleep(click_pause)
    
def make_text(data):
    print('make_text')
    pyperclip.copy(data['text'])
    ctrl_v()
def make_header(data):
    print('make_header')
    pyperclip.copy('/')
    ctrl_v()
    time.sleep(click_pause)
    pyperclip.copy('title')
    ctrl_v()
    pag.press('tab')
    time.sleep(click_pause)
    pyperclip.copy(data['text'])
    ctrl_v()
def make_picture(data):
    pyperclip.copy(data['text'])
    ctrl_v()
def make_incut(data):
    print('make_incut')
    pyperclip.copy('/')
    ctrl_v()
    time.sleep(click_pause)
    pyperclip.copy('subheading')
    ctrl_v()
    pag.press('tab')
    pyperclip.copy('/')
    ctrl_v()
    time.sleep(click_pause)
    pyperclip.copy('blue')
    ctrl_v()
    pag.press('tab')
    time.sleep(click_pause)
    pyperclip.copy(data['text'])
    ctrl_v()
def make_list(data):
    print('make_list')
    pyperclip.copy('/')
    ctrl_v()
    time.sleep(click_pause)
    pyperclip.copy('bulleted')
    ctrl_v()
    pag.press('tab')
    time.sleep(click_pause)
    text = data['items']
    for i in range(len(text)):
        pyperclip.copy(text[i])
        ctrl_v()
        if len(text)-1 == i:
            print('last')
        else:
            pag.press('enter')
        time.sleep(click_pause*2)
def make_delimiter(data):
    print('make_delimiter')
    pyperclip.copy('/')
    ctrl_v()
    time.sleep(click_pause)
    pyperclip.copy('dots divider')
    ctrl_v()
    pag.press('tab')
    time.sleep(click_pause)
    
def click(_x,_y):
    pag.moveTo(x=_x,y=_y)
    pag.mouseDown()
    #time.sleep(click_pause)
    pag.mouseUp()
def move_down():
    pag.scroll(-10000)
    click(900,1000)
def scroll_up():
    pag.scroll(10000)
    time.sleep(click_pause*5)
def ctrl_v():
    pag.keyDown('ctrl')
    pag.press('v')
    time.sleep(0.1)
    pag.keyUp('ctrl')


def link_inizialization():
    print('link_inizialization')
    links = myl.links()
    for i in range(len(links)):
        links[i] = links[i].split('/')[-1].split('-')[0]
    return links

def find_subsite(subsite):
    subsite_finded = False
    for s in list_subsite:
        if subsite == s:
            subsite_finded = True
    if subsite_finded:
        pyperclip.copy(subsite)
    else:
        pyperclip.copy('Свой блог')

def change_to_default(bt):
    print('change_to_default')
    if lastblock == 'incut' and bt != 'incut':
        pyperclip.copy('/')
        ctrl_v()
        time.sleep(click_pause)
        pyperclip.copy('default')
        ctrl_v()
        pag.press('tab')
    #if lastblock == 'bulleted' and bt != 'bulleted':
       #pag.press('enter')

def output_mouse_coordinates():
    try:
        while True:
            x, y = pag.position()
            positionStr = 'X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4)
            print(positionStr, end = '')
            print('\b'*len(positionStr), end = '', flush = True)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('\nГотово!')























#params = (
#    ('subsiteId', '256444'),
#    ('contentId', '1113147'),
#    ('sorting', 'hotness'),)
#response = requests.get('https://api.dtf.ru/v2.1/comments', headers=headers, params=params)
#print(todos['result']['commentsSeenCount'])
