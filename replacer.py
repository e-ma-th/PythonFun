def main():
    try:
        reader = open('BeeMovieScript.txt', 'r').readlines()
        final = open('CumMovieScript.txt','w')
    except FileNotFoundError:
        print("there is no file with this name")
    output = ""

    replacements = {
        "bee":"cum",
        "Bee":"Cum",
        "Coming":"Cuming",
        "coming":"cuming",
        "Come":"Cum",
        "come":"cum",
        "honey":"jizz",
        "Honey":"Jizz"
    }
    for i in reader:
        change = False
        for j in replacements:
            if i.replace(j,replacements[j]) != i:
                output += i.replace(j,replacements[j])
                change = True
        if not(change):
            output += i
    final.write(output)

if __name__ == '__main__':
    main()