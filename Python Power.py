import pandas as pd
import pyautogui
import time
# pyautogui.write
# pyautogui.press
# pyautogui.click
# pyautogui.hostkey -> combinação
pyautogui.PAUSE = 1
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=427, y=358)
time.sleep(3)
pyautogui.write("teste.gmail")
time.sleep(2)
pyautogui.press("tab")
time.sleep(5)
pyautogui.write("macauly")
time.sleep(3)
pyautogui.click(x=677, y=520)
time.sleep(2)

tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
    print(linha)
    pyautogui.click(x=541, y=240)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.scroll(10000)
