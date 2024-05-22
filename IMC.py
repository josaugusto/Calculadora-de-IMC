import PySimpleGUI as sg

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def check_imc(imc):
    if imc < 18.5:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Baixo peso".replace(".", ","))
    elif imc >= 18.6 and imc <= 24.9:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Peso Normal".replace(".", ","))
    elif imc >= 25 and imc <= 29.9:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Sobrepeso".replace(".", ","))
    elif imc >= 30 and imc <= 34.9:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Obesidade grau I".replace(".", ","))
    elif imc >= 35 and imc <= 39.9:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Obesidade grau II".replace(".", ","))
    else:
        print(f"Seu índice de massa corporal é igual a: {round(imc, 2)}; Classificado como: Obesidade grau III".replace(".", ","))

def main():

    # Tema
    sg.theme("DarkBlue2")

    layout_imc = [
        [sg.Text("Informe sua altura(m): "), sg.Multiline(key="altura", size=(15, 1))],
        [sg.Text("Informe seu peso(Kg): "), sg.Multiline(key="peso", size=(15, 1))],
        [sg.Button("Calcular")],
        [sg.Text("Segundo a OMS(Organização Mundial de Saúde):")],
        [sg.Multiline(size=(40, 10), reroute_stdout=True, do_not_clear=False)]

    ]

    janela_imc = sg.Window("Calculadora IMC", layout_imc, size=(320, 200))

    while True:
        evento, valores = janela_imc.read()
        if evento == sg.WINDOW_CLOSED:
            break
        elif evento == "Calcular":
            if valores["altura"] == '' or valores["peso"] == '':
                sg.popup("Erro, preencha os campos de altura e peso!", title="Erro")
            elif not(isfloat(str(valores["altura"]).replace(",", "."))):
                sg.popup("Erro, altura inválida!")
            elif not(isfloat(str(valores["peso"]).replace(",", "."))):
                sg.popup("Erro, peso inválido!")
            else:
                check_imc(float(valores["peso"].replace(',', '.')) / float(valores["altura"].replace(',', '.'))**2)
main()
