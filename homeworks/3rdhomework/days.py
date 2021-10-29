from PIL import Image

Mo = Image.open('monday.jpg')
Tu = Image.open('tuesday.jpg')
We = Image.open('wednesday.jpg')
Th = Image.open('thursday.jpg')
Fr = Image.open('friday.jpg')
Sa = Image.open('saturday.jpg')
Su = Image.open('sunday.jpg')

while True:
    day = input('if you want to quit the loop type exit\nwhat day is today?\nyou should type either of mo, tu, we, th, fr, sa or su\n>>> ')
    if day == 'mo':
        print('happy monday!')
        Mo.show()
        break
    elif day == 'tu':
        print('happy tuesday!')
        Tu.show()
        break
    elif day == 'we':
        print('happy wednesday!')
        We.show()
        break
    elif day == 'th':
        print('happy thursday!')
        Th.show()
        break
    elif day == 'fr':
        print('happy friday!')
        Fr.show()
        break
    elif day == 'sa':
        print('happy saturday!')
        Sa.show()
        break
    elif day == 'su':
        print('happy sunday!')
        Su.show()
        break
    elif day == 'exit':
        break