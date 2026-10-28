def bottle_song():
	# write your code here!
    # Write a program that can print the song "99 Bottles of Beer".
    # number of beer, nonplural/plural form of bottles, print the lyrics for the number of bottles left
    bottle_count = 99
    next_count = bottle_count - 1
    plural = "s"
    plural_next = "s"
    singular = ""
    
    for i in range(99):
        if bottle_count == 1:
            lyrics = "1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall."
            print(lyrics)
        else:
            lyrics = f"{bottle_count} bottle{plural} of beer on the wall, {bottle_count} bottle{plural} of beer. Take one down and pass it around, {next_count} bottle{plural_next} of beer on the wall."
            # print (i)
            print(lyrics)
            bottle_count-= 1
            next_count-= 1
            if bottle_count == 1:
                plural = singular
            if next_count == 1:
                plural_next = singular
            elif next_count == 0:
                plural_next = "s"


bottle_song()

####kldjsfalkfdajalskdfjdfls