import frappe


@frappe.whitelist(allow_guest=True, xss_safe=True, methods=["GET"])
def get_school_tuition():
	try:
		school_tuition = frappe.get_single("School Tuition")
		return {"success": True, "data": school_tuition}
	except Exception as e:
		frappe.log_error(e)
		return {"success": False}
