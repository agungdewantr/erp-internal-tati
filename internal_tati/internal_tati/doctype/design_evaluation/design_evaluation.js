frappe.listview_settings['Design Request'] = {
    add_fields: ['name', 'title', 'requested_by', 'purpose'],
    get_indicator: function(doc) {
        return [__("Pending"), "orange", "status,=,Pending"];
    },
    onload: function (listview) {
        listview.page.add_inner_button(__('Evaluate Request'), function () {
            let selected_docs = listview.get_checked_items();

            if (selected_docs.length === 0) {
                frappe.msgprint(__('Please select at least one Design Request.'));
                return;
            }

            selected_docs.forEach(doc => {
                frappe.call({
                    method: "frappe.client.insert",
                    args: {
                        doc: {
                            doctype: "Design Evaluation",
                            design_request: doc.name, // Prefill Design Request
                            requester: doc.requested_by,
                            purpose: doc.purpose
                        }
                    },
                    callback: function (r) {
                        if (!r.exc) {
                            frappe.set_route("Form", "Design Evaluation", r.message.name);
                        }
                    }
                });
            });
        });
    }
};
