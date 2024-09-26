from odoo import http
from odoo.http import request


class PersonsController(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def persons_page(self, **kw):
        persons = request.env["persons.person"].search([], limit=5)
        return request.render(
            "persons_module.persons_template",
            {
                "persons": persons,
            },
        )

    @http.route(
        "/persons/create",
        type="http",
        auth="public",
        website=True,
        methods=["GET"]
    )
    def person_form(self, **kwargs):
        return request.render("persons_module.person_form")

    @http.route(
        "/persons/create",
        type="http",
        auth="public",
        website=True,
        methods=["POST"],
        csrf=False,
    )
    def create_person(self, **post):
        request.env["persons.person"].sudo().create(
            {
                "first_name": post.get("first_name"),
                "last_name": post.get("last_name"),
                "birthday": post.get("birthday"),
                "sex": post.get("sex"),
                "company_id": request.env.company.id,
            }
        )
        return request.redirect("/persons")
