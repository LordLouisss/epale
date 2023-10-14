meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict["LOL"])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("esta palabra no existe en el diccionario")
    # ¿Qué hacer si no se encuentra la palabra?
