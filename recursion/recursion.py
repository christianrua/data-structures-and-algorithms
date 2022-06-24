

counter = 0
def inception(counter):
    if counter > 4:
        return 'done!'

    counter += 1
    return inception(counter)

print(inception(counter))