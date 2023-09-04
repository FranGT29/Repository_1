def metros_pulgadas(metros):
    return metros*39.37
def pulgadas_metros(pulgadas):
    return pulgadas/12
if __name__=='__main__':
    metros=int(input('ingresa la cantidad de metros: '))
    pulgadas=metros_pulgadas(metros)
    print(f'{metros} metros equivale a {pulgadas:.2f} pulgadas')