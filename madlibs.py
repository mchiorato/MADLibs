# teste de variaveis e tambem como escrever o formato

marcos = "teste"

#tres formas de escrever texto e usar variaveis
print("subscribe to " + marcos)
print("subscribe to {}".format(marcos))
print(f"subscribe to {marcos}")

adj = input("Adjective: ")
verb1 = input("Verbo 1: ")
verb2 = input("Verbo 2: ")
famous_person = input("Pessoa Famosa: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)