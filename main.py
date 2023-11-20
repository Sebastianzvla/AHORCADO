import random #PARA UTILIZAR LOS COMANDOS DE RANDOM
import hangman_art
import hangman_words
from replit import clear

Display = [] # DECLARA LA LISTA LLAMADA DISPLAY
Meta = False 
vida = 6

print(hangman_art.logo+"\n")
Respuesta = input("Te gustaria elegir una palabra aleatoria?(si/no) ").lower() 
if (Respuesta == "si"):
     P_Elegida = random.choice(hangman_words.P_aleatoria) #ELIGE UNA PALABRA ALEATORIA
     #print(f"La palabra aleatoria es: {P_Elegida}") #MOSTRAR PALABRA AL INICIO 
else:
  P_Elegida = input("Que palabra te gustaria elegir? ").lower()

for x in P_Elegida:
  Display.append("_") # COLOCA "_" EN CADA POSICION DE LA LISTA DISPLAY
print(hangman_art.stages[6])
print(Display)

while not Meta == True:
  count = 0
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in Display:
    print("Ya habias escodigo esa palabra")
  for letter in P_Elegida:
    if letter == guess:
      Display.pop(count)
      Display.insert(count, guess)
    count += 1  
  if guess not in Display:
      vida -=1
      print(f"Te quedan {vida} vidas\n")
  if "_" not in Display:
    Meta = True
    print("Felicidades Ganaste!!")
  elif vida == 0:
    Meta = True
    print("Perdiste!!")
    print(f"La palabra era: {P_Elegida}")
    print(hangman_art.stages[vida])
    break
     
  print(hangman_art.stages[vida])
  print(Display)
