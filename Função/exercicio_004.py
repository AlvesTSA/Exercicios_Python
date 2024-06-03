"""/*4. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3.P .R3).*/
"""

def calc_vol(r):
    pi = 3.14159265358979323846
    v = (4.0/3.0)*pi*r*r*r

    return v

r = float(input("Informe o raio da esfera: "))
v = calc_vol(r)

print(f"Volume da esfera: {v:.2f}")