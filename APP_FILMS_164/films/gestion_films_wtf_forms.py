"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from APP_FILMS_164.database.database_tools import DBconnection
from wtforms.widgets import TextArea


class FormWTFAddFilm(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_film_regexp = ""

    nom_chantier_add = StringField("Nom du chantier")
    nom_projet_add = StringField("Nom du projet")


    with DBconnection() as mc_afficher:
        sql_liste_clients = """ SELECT id_clients,nom_clients FROM t_clients ORDER BY nom_clients """
        mc_afficher.execute(sql_liste_clients)
        liste_clients = mc_afficher.fetchall()

        options = []
        for resultat in liste_clients:
            id_clients = resultat['id_clients']
            nom_film = resultat['nom_clients']
            options.append((id_clients, nom_film))


    nom_client = SelectField("Nom du client", choices=options)

    submit = SubmitField("Enregistrer")


class FormWTFUpdateFilm(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.

    """
    with DBconnection() as mc_afficher:
        """ on va aller chercher les clients dans la DB pour les afficher dans le champ de selection """
        sql_liste_clients = """ SELECT id_clients,nom_clients FROM t_clients ORDER BY nom_clients """
        mc_afficher.execute(sql_liste_clients)
        liste_clients = mc_afficher.fetchall()

        options = []
        for resultat in liste_clients:
            id_clients = resultat['id_clients']
            nom_film = resultat['nom_clients']
            options.append((id_clients, nom_film))


    nom_client = SelectField("Nom du client", choices=options)

    nom_film_update_wtf = StringField("Nom du chantier")
    nom_chantier = StringField("Nom du chantier")
    nom_projet = StringField("Nom du projet")
    """
    duree_film_update_wtf = IntegerField("Durée du film (minutes)", validators=[NumberRange(min=1, max=5000,
                                                                                            message=u"Min %(min)d et "
                                                                                                    u"max %(max)d "
                                                                                                    u"Selon Wikipédia "
                                                                                                    u"L'Incendie du "
                                                                                                    u"monastère du "
                                                                                                    u"Lotus rouge "
                                                                                                    u"durée 1620 "
                                                                                                    u"min")])
    """
    #description_film_update_wtf = StringField("Description du film ", widget=TextArea())
    #cover_link_film_update_wtf = StringField("Lien de l'affiche du film ", widget=TextArea())
    #datesortie_film_update_wtf = DateField("Date de sortie du film", validators=[InputRequired("Date obligatoire"),
    #                                                                             DataRequired("Date non valide")])
    submit = SubmitField("Valider")


class FormWTFDeleteFilm(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_film_delete_wtf = StringField("Effacer ce devis")
    submit_btn_del_film = SubmitField("Effacer devis")
    submit_btn_conf_del_film = SubmitField("Valider la suppression du devis")
    submit_btn_annuler = SubmitField("Annuler")
