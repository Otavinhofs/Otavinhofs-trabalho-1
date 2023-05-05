from Desktop import Desktop
from Notebook import Notebook

meuDesktop = Desktop("Dell", "Preto", 3000.0, 500)
meuNotebook = Notebook("Lenovo", "Branco", 2500.0, 4)

print(meuDesktop.getInformacoes())
print(meuNotebook.getInformacoes())
print('===============================')
print(meuDesktop.cadastrar())
print(meuNotebook.cadastrar())
