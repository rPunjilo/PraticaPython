def arquivoExiste(arq):
    try:
        s = open(arq, 'rt')
        s.close()
    except FileNotFoundError:
        return("Arquivo não encontrado")
    else:
        return("Arquivo foi encontrado!")








