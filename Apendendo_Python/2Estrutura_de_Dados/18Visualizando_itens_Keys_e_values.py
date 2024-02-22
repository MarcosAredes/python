aluno = {
    "nome": "ana",
    "idade": 16,
    "nota final": "A",
    "situação": "aprovada",
    "materias": ["geografia", "historia", "artes"],
}

print(aluno.items())  # items
# print(aluno.get("materias"))  # values
print(aluno.values())
# print(len(aluno))  # Keys
print(aluno.keys())  # Keys

"""
resultado:

dict_items([('nome', 'ana'), ('idade', 16), ('nota final', 'A'), ('situação', 'aprovada'), ('materias', ['geografia', 'historia', 'artes'])])
dict_values(['ana', 16, 'A', 'aprovada', ['geografia', 'historia', 'artes']])
dict_keys(['nome', 'idade', 'nota final', 'situação', 'materias'])

"""
