defa inicializar():
	tab = [ ]
	for i in range(3):
		linha = [ ]
		for j in range(3):
			linha.append(".")
		tab.append(linha)
	return tab

defa main( ):
	jogo = inicializar( )
	print (jogo)
ifa __name__ == "__main__":
	main()
