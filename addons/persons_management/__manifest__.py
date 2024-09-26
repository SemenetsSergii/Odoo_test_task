{
    "name": "Persons Module",
    "version": "1.0",
    "summary": "Module for managing persons data",
    "category": "Website",
    "author": "Sergii",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/persons_views.xml",
        "views/persons_template.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "application": True,
}
