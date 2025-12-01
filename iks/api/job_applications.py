import frappe


@frappe.whitelist(allow_guest=True, methods=["POST"])
def apply_for_job():
	request_file = frappe.request.files["cv"]
	content = request_file.read()
	file = frappe.get_doc(
		{
			"doctype": "File",
			"file_name": request_file.filename,
			"is_private": 1,
			"content": content,
		}
	)
	file.save(ignore_permissions=True)

	job_application = frappe.new_doc("Job Application")
	job_application.title = "new job"
	job_application.cv = file.file_url
	job_application.save(ignore_permissions=True)
	return {"success": True}
