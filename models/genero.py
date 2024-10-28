# -*- coding: utf-8 -*-
from tokenize import String

from odoo import models, fields


class genero(models.Model):
    _name = "filmotecaalvaro.genero"
    _description = "filmotecaalvaro.genero"

    name = fields.Char(string="Nombre", read_only=False, required=True, help="Nombre del género.")
    description = fields.Text(string="Descripción")

    peliculas_id = fields.One2many(String = "Películas", comodel_name="filmotecaalvaro.pelicula", inverse_name="genero_id")