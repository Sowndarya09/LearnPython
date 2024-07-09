def translate(phrase):
    translation =""
    for ph in phrase:
        if ph in "AEIOUaeiou":
            ph="g"
            translation=translation+ph
        else:
            translation = translation+ph
    return translation

print(translate("Sownd arya"))