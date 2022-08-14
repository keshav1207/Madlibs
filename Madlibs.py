file = open('madlibs.txt', 'r')
content = file.read()

Adjective = input('Enter an adjective:    ').lower()
Noun = input('Enter a noun:    ').lower()
Verb = input('Enter a verb:   ').lower()

Original = ['ADJECTIVE', 'NOUN', 'VERB']
Replacement = [ Adjective, Noun, Verb]

for i in range(len(Original)):
    content = content.replace(Original[i], Replacement[i])

new_file = open('madlibs2.txt','w')
new_file.write(content)
new_file.close()