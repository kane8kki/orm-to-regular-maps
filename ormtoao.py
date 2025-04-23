from PIL import Image
orm = int(input("ao-1, roughness-2, metalness-3"))
if orm == 1: 
    texture_name = input("texture name (must be in the same directory as the program) ex : texture.png")

    orm_image = Image.open(texture_name)

    # Sépare les canaux R, G, B
    r, g, b = orm_image.split()

    # Crée une nouvelle image RGB avec R comme AO, G et B à 0 (ou juste en niveaux de gris)
    ao_image = Image.merge("RGB", (r, r, r))  # ou Image.merge("RGB", (r, r, r)) pour un visuel gris

    # Sauvegarde l'image AO
    ao_image.save("texture_ao.png")
    print("ambient occlusion map saved !")
    saved = 1
    
if orm == 2: 
    texture_name = input("texture name (must be in the same directory as the program) ex : texture.png")
    # Charge l'image ORM
    orm_image = Image.open(texture_name)

    # Sépare les canaux R, G, B
    r, g, b = orm_image.split()

    # Crée une nouvelle image RGB avec R comme AO, G et B à 0 (ou juste en niveaux de gris)
    ao_image = Image.merge("RGB", (g, g, g))  # ou Image.merge("RGB", (r, r, r)) pour un visuel gris

    # Sauvegarde l'image AO
    ao_image.save("texture_roughness.png")
    print("roughmap saved !")
    saved = 1

if orm == 3: 
    texture_name = input("texture name (must be in the same directory as the program) ex : texture.png")
    # Charge l'image ORM
    orm_image = Image.open(texture_name)

    # Sépare les canaux R, G, B
    r, g, b = orm_image.split()

    # Crée une nouvelle image RGB avec R comme AO, G et B à 0 (ou juste en niveaux de gris)
    ao_image = Image.merge("RGB", (b, b, b))  # ou Image.merge("RGB", (r, r, r)) pour un visuel gris

    # Sauvegarde l'image AO
    ao_image.save("texture_metalness.png")
    print("metalmap saved !")
    saved = 1

else : 
    if not saved == 1:
        print("error, not correct value")
