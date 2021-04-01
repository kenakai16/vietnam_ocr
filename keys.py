import pickle as pkl

alphabet_list = pkl.load(open('char.pkl','rb'))
alphabet = [ord(ch) for ch in alphabet_list]
alphabet_v2 = alphabet
# print(alphabet_v2)
print(alphabet_list)
