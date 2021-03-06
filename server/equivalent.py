from enum import Enum
import datetime

start = "Votre panier est équivalent à "

travel_cfp = {0.8: ["TGV", "Paris-Lille"],
              1.1: ["TGV", "Paris-Rennes"],
              1.5: ["TGV", "Paris-Strasbourg"],
              1.7: ["TGV", "Paris-Lyon"],
              1.9: ["TGV", "Paris-Bordeaux"],
              2.5: ["TGV", "Paris-Montpellier"],
              2.6: ["TGV", "Paris-Marseille"],
              3.3: ["TGV", "Paris-Nice"],
              4.2: ["Eurostar", "Paris-Londres"],
              4.5: ["voiture", "Paris-Aéroport Charles De Gaulles"],
              4.9: ["TGV", "Marseille-Le Havre"],
              6.7: ["voiture", "Genève Annecy"],
              7.2: ["voiture", "Paris-Disneyland"],
              9.2: ["TER", "Clermont Ferrand-Nîmes"],
              10.2: ["voiture", "Lyon-Saint-Etienne"],
              10.7: ["voiture", "Paris-Fontainebleau"],
              15.3: ["TER", "Paris-Lyon"],
              15.6: ["voiture", "Avignon-Montpellier"],
              17.2: ["voiture", "Lyon-Grenoble"],
              22.6: ["voiture", "Lyon-Annecy"],
              35.6: ["voiture", "Paris-Lille"],
              56.4: ["voiture", "Paris-Rennes"],
              72.3: ["voiture", "Paris-Londres"],
              75.2: ["voiture", "Paris-Lyon"],
              79.3: ["voiture", "Paris-Strasbourg"],
              94.7: ["voiture", "Paris-Bordeaux"],
              121.4: ["voiture", "Paris-Montpellier"],
              125.6: ["voiture", "Paris-Marseille"],
              151.3: ["voiture", "Paris-Nice"]}

# ajout des aller-retour dans la liste pour varier les équivalents
travel_cfp_2 = {}
for el in travel_cfp:
    key = 2 * el
    travel_cfp_2[key] = travel_cfp[el].copy()
    # on ajoute 1 pour dire que c'est un trajet
    travel_cfp[el].append(1)
    # on ajoute 2 pour dire que c'est 2 trajets soit un aller-retour
    travel_cfp_2[key].append(2)

# fusion en un seul dictionnaire
travel_cfp_final = {**travel_cfp, **travel_cfp_2}

# on récupère les clefs du dictionnaire qui sont les empreintes carbonnes équivalentes
travel_keys = list(travel_cfp_final.keys())
travel_keys.sort()


# food_cfp = {283: "Inde",
#             640: "Chine",
#             644: "Japon",
#             822: "Corée du Sud",
#             989: "Espagne",
#             1008: "Russie",
#             1062: "Royaume-Unis",
#             1066: "Allemagne",
#             1206: "Italie",
#             1357: "Suisse",
#             1420: "France",
#             1617: "Brésil",
#             1719: "Etats-Unis",
#             1939: "Australie" }


def convert_days_to_date(nb_days):
    years = nb_days // 365
    nb_days = nb_days % 365
    months = nb_days // 30
    nb_days = nb_days % 30
    days = nb_days
    return [int(years), int(months), int(days)]


def make_travel_equiv(cfp):
    close_cfp = 0
    # on recherche l'empreinte carbone la plus proche de notre entrée cfp
    for el in travel_keys:
        if cfp > el:
            close_cfp = el
    if close_cfp == 0:
        return -1
    else:
        equiv = travel_cfp_final[close_cfp]
        if equiv[2] == 1:
            return "Votre panier est équivalent à un trajet " + equiv[1] + " en " + equiv[0]
        else:
            return "Votre panier est équivalent à un aller-retour " + equiv[1] + " en " + equiv[0]


def make_tree_equiv(cfp):
    ref_cfp = 25
    equiv = convert_days_to_date(round((cfp * 365) / ref_cfp, 0))
    result = ""
    if equiv[0] != 0:
        result = "Il faudra " + str(equiv[0]) + " an" + ("", "s")[equiv[0] > 2]
        result += (("", " et " + str(equiv[2]) + " jour" + ("", "s")[equiv[2] > 2])[equiv[2] > 0],
                   " et " + str(equiv[1]) + " mois")[equiv[1] > 0]
    elif equiv[1] != 0:
        result = "Il faudra " + str(equiv[1]) + " mois"
        result += ("", " et " + str(equiv[2]) + " jour" + ("", "s")[equiv[2] > 2])[equiv[2] > 0]
    elif equiv[2] != 0:
        result = "Il faudra " + str(equiv[2]) + " jour" + ("", "s")[equiv[2] > 2]
    else:
        return -1
    result += " à un arbre pour absorber l'empreinte carbone de votre panier"
    return result


def make_money_equiv(cfp):
    ref_cfp = 0.024
    equiv = ref_cfp * cfp
    if round(equiv, 2) == 0:
        return -1
    else:
        return "Il faudrait faire un don de " + str(
            round(equiv, 2)) + "€ pour compenser l'empreinte carbone de votre panier"


def make_delta_avg_equiv(cfp):
    ref_cfp = 1420
    equiv = (cfp * 52) / ref_cfp
    if round(equiv, 1) != 1:
        return "Si vous consommez le même panier toutes les semaines pour une seule personne, alors vous consommez " + \
               (str(round(equiv, 1)), str(round(1 / equiv, 1)))[equiv < 1] + " fois " + ("plus ", "moins ")[
                   equiv < 1] + "que la moyenne française"
    else:
        return "Si vous consommez le même panier toutes les semaines pour une seule personne, alors êtes dans la consommation française moyenne"


def get_equiv_carbone(cfp_kg):
    """
    :param cfp_kg: cfp est en kg CO2/kg aliment
    :return:
    """

    equivalents = []

    if cfp_kg > 0:
        # travel
        if make_travel_equiv(cfp_kg) != -1:
            equivalents.append({"name": "travel", "text": make_travel_equiv(cfp_kg)})

        # tree
        if make_tree_equiv(cfp_kg) != -1:
            equivalents.append({"name": "tree", "text": make_tree_equiv(cfp_kg)})

        # money to compensate
        if make_money_equiv(cfp_kg) != -1:
            equivalents.append({"name": "money", "text": make_money_equiv(cfp_kg)})

        # delta french average
        equivalents.append({"name": "delta_avg", "text": make_delta_avg_equiv(cfp_kg)})

    return equivalents


if __name__ == "__main__":
    cfp = 1.720747407407407
    cfp1 = 14
    print(make_travel_equiv(cfp1))
    print(make_tree_equiv(cfp))
    print(make_money_equiv(cfp))
    print(make_delta_avg_equiv(cfp1))
