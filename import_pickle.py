import pickle
f = open('utenti.dump', 'rb')
utenti = pickle.load(f)
print (utenti)