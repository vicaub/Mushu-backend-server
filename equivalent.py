

def get_equiv_carbone(model, cfp):
    #cfp est en kg CO2/kg aliment
    equiv = 0
    cfp_model = 0
    result = "votre panier est équivalent à "
    if model == "train": cfp_model = 2.6
    elif model == "plane": cfp_model = 430
    elif model == "email": cfp_model = 0.004
    elif model == "tree": cfp_model = 25
    elif model == "electricity": cfp_model = 0.09
    else : return "modèle invalide"
    equiv = round(cfp/cfp_model,1)

    if model == "train": result += str(equiv) + " trajet" + (" ", "s ")[equiv > 2.0] + "Paris-Marseille en TGV"
    elif model == "plane": result += str(equiv) + " vol" + (" ", "s ")[equiv > 2.0] + "Paris-New York"
    elif model == "email": result += "l'envoie de " + str(equiv) + " email" + (" ", "s ")[equiv > 2.0]
    elif model == "tree": result += "la consommation en carbone de 1 arbre en " + (str(int(equiv)) + " an", str(round(equiv * 12,1)) + " mois") [equiv < 1] + ("", "s") [equiv > 2.0]
    elif model == "electricity": result += "la consommation en carbone pour " + str(equiv) + " kWh d'électricité, soit la consommation d'une ampoule basse-consommation allumée pendant " + str(round(equiv*5/22,1)) + " heure" + ("", "s")[equiv > 2.0]
    return result


def get_equiv_carbone(cfp):
    <

if __name__ == "__main__":
    cfp = 1.7207407407407407
    print(get_equiv_carbone("email", cfp))