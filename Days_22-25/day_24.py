# Day 24 of 100 Days of Code Challenge
# Mail merge

# create list with names in name file
with open(file='day_24_names.txt', mode='r+') as file:
    text = file.read()
    names = text.splitlines()

# create new files with each item in names list while also replacing the [name] placeholder
with open('day_24_letter.txt', 'r') as file:
    text = file.read()
    for name in names:
        data = text.replace('[name]', name)
        with open(f'day_24_{name}.txt', 'w') as complete_file:
            complete_file.write(data)
