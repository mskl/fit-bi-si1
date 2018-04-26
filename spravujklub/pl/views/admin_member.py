from flask import request, render_template
from main import app, member_controller


@app.route('/admin_member', methods=['GET'])
def admin_member():
    """Admin panel to manage members"""
    name = request.values.get("name")
    email = request.values.get("mail")
    password = request.values.get("password")
    delete_id = request.values.get("delete")

    if name is not None and email is not None:
        try:
            member_controller.create_member(name=name, mail=email, password=password)
        except Exception as ex:
            print(str(ex))

    if delete_id is not None:
        try:
            delete_id = int(delete_id)
            member_to_delete = member_controller.get_member_by_id(delete_id)
            member_controller.delete_member(member_to_delete)
        except Exception as ex:
            print(str(ex))

    # Render the template
    return render_template("admin_member.html", members=member_controller.get_all_members(), title="Member admin")