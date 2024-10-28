# -*- coding: utf-8 -*-

from odoo import models, fields


class pelicula(models.Model):
    # Los nombres de los modelos son: "nombre módulo"."nombre clase"
    # Es un campo obligatorio.
    _name = "filmotecaalvaro.pelicula"
    _description = "filmotecaalvaro.pelicula"

    # Campos:
    name = fields.Char(string="Nombre", read_only=False, required=True, help="Nombre de la película")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha")
    start_date = fields.Datetime()
    end_date = fields.Datetime(compute="_get_end_date", store=True)
    is_spanish = fields.Boolean(string="Española")

    # Relaciones:
    genero_id = fields.Many2one("filmotecaalvaro.genero", string="Género", required=True, ondelete="cascade")