import frappe
import json

def create_workspace():
    if not frappe.db.exists('Workspace', 'Internal Tati'):
        try:
            workspace = frappe.get_doc({
                'doctype': 'Workspace',
                'name': 'Internal Tati',
                'module': 'Internal Tati',
                'public': 1,
                'for_user': '',
                'label': 'Internal Tati',
                'title': 'Internal Tati',
                'icon': 'color-energy-points',
                'content': json.dumps([
                        {
                            "id": "VjStFcIEME",
                            "type": "header",
                            "data": {
                                "text": "<span class=\"h4\">Internal Tati</span>",
                                "col": 12
                            }
                        },
                        {
                            "id": "SgNWi3Wezz",
                            "type": "card",
                            "data": {
                                "card_name": "Marketing",
                                "col": 4
                            }
                        }
                    ]),
                'links': [
                    {
                        "type": "Card Break",
                        "label": "Marketing",
                        "link_type": "DocType",
                        "link_count": 1,
                        "parent": "Internal Tati",
                        "parentfield": "links",
                        "parenttype": "Workspace",
                    },
                    {
                        "type": "Link",
                        "label": "Design Request",
                        "link_type": "DocType",
                        "link_to": "Design Request",
                        "link_count": 0,
                        "parent": "Internal Tati",
                        "parentfield": "links",
                        "parenttype": "Workspace",
                    },
                ]
            })
            workspace.insert()
            frappe.db.commit()
        except Exception as e:
            print(f"Error occurred: {e}")
