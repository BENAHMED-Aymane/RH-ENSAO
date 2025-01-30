from odoo import models, fields, api

class Employe(models.Model):
    _name = 'rh.employe'
    _description = "Employe"

    nom_complet = fields.Char(string="Nom complet", required=True)
    matricule = fields.Char(string="Matricule", required=True, unique=True)
    date_naissance = fields.Date(string="Date de naissance")
    email = fields.Char(string="E-mail professionnel")
    telephone = fields.Char(string="Numéro de téléphone")
    adresse = fields.Char(string="Adresse personnelle")
    #poste_id = fields.Many2one('rh.poste', string="Poste occupé")
    #departement_id = fields.Many2one('rh.departement', string="Département assigné")
    date_embauche = fields.Date(string="Date d'embauche")
    salaire = fields.Float(string="Salaire")
    statut = fields.Selection([
        ('actif', 'Actif'),
        ('inactif', 'Inactif')
    ], string="Statut", default='actif')
    photo = fields.Image(string="Photo")
    #documents_ids = fields.One2many('rh.document', 'employe_id', string="Documents attachés")
    #historique_postes = fields.One2many('rh.historique.poste', 'employe_id', string="Historique des postes")

    _sql_constraints = [
        ('matricule_unique', 'UNIQUE(matricule)', 'Le matricule doit être unique!'),
    ]
