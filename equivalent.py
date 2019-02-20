from enum import Enum

start = "Votre panier est équivalent à "

# TODO: voir problème tree equiv et electricity equiv (une ampouble basse conso fait du 100W max...)
# TODO: calculer distance equiv en avion, train et voiture puis trouver un équivalent d'itinéraire
# TODO: voir réponses formulaire

def make_train_equiv(cfp_kg):
    cfp_model = 2.6
    equiv = cfp_kg / cfp_model
    text = start + str(round(equiv)) + " trajet" + (" ", "s ")[equiv > 2.0] + "Paris-Marseille en TGV"
    return {"value": equiv, "text": text}


def make_plane_equiv(cfp_kg):
    cfp_model = 430
    equiv = cfp_kg / cfp_model
    text = start + str(round(equiv)) + " vol" + (" ", "s ")[equiv > 2.0] + "Paris-New York"
    return {"value": equiv, "text": text}


def make_email_equiv(cfp_kg):
    cfp_model = 0.004
    equiv = cfp_kg / cfp_model
    text = start + "l'envoi de " + str(round(equiv)) + " email" + (" ", "s ")[equiv > 2.0]
    return {"value": equiv, "text": text}


def make_tree_equiv(cfp_kg):
    cfp_model = 25
    equiv = cfp_kg / cfp_model
    text = start + "??????la consommation en carbone de 1 arbre en " + \
           (str((round(equiv, 1))) + " an", str(round(equiv * 12, 1)) + " mois")[equiv < 1] + ("", "s")[equiv > 2.0]
    return {"value": equiv, "text": text}


def make_electricity_equiv(cfp_kg):
    cfp_model = 0.09
    equiv = cfp_kg / cfp_model
    text = start + "la consommation en carbone pour " + str(
        round(
            equiv)) + " kWh d'électricité, soit la consommation d'une ampoule basse-consommation allumée pendant " + str(
        round(equiv * 5 / 22)) + " heure????" + ("", "s")[equiv > 2.0] + " pas convaincu par l'équivalent en heure"
    return {"value": equiv, "text": text}


def get_equiv_carbone(cfp_kg):
    """
    :param cfp_kg: cfp est en kg CO2/kg aliment
    :return:
    """

    json = dict()

    # train
    json["train"] = make_train_equiv(cfp_kg)

    # plane
    json["plane"] = make_plane_equiv(cfp_kg)

    # email
    json["email"] = make_email_equiv(cfp_kg)

    # tree
    json["tree"] = make_tree_equiv(cfp_kg)

    # electricity
    json["electricity"] = make_electricity_equiv(cfp_kg)

    return json


if __name__ == "__main__":
    cfp = 1.7207407407407407
    print(get_equiv_carbone(cfp))
