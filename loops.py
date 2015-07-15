def bottles_lyrics(bottlecount = 99):
    # because we're 'passing in' bottlecount as an argument,
    # we no longer need to define it inside the function.
    for bottle in range(bottlecount,0,-2):
        print(str(bottle) + " bottles of beer on the wall,")
        print(str(bottle) + " bottles of beer,")
        print("take one down, pass it around,")
        print(str(bottle - 2) + " bottles of beer on the wall!")
    return None
bottles_lyrics(8)
def bottles_lyrics(bottle = 99):
    bottle = 9
    while bottle > 0:
        if bottle is 1:
            word = "bottle"
        else:
            word = "bottles"
        print(str(bottle) + word + " of beer on the wall,")
        print(str(bottle) + word + " bottle of beer,")
bottle = 2
if bottle%2==0:
    print ("it's even!)")
elif bottle < 5:
    print('almost out!')
elif bottle < 10:
    print('running low!')
else:
    print("that's odd!")