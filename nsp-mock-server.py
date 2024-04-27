from flask import Flask, jsonify, request
import json


app = Flask(__name__)

members_data = json.load(open('nsp_members.json','r'))



@app.route("/members", methods=["https://docs.google.com/spreadsheets/d/1sweUf_oFxKinoJQaK5U6CKVakNRD-j_xx6jkIW58TDk/edit#gid=0GET"])
def get_members():
    return jsonify(members_data)


@app.route("/members/<member_id>", methods=["GET"])
def get_member(member_id):
    for member in members_data:
        if member["id"] == member_id:
            return jsonify(member)
    return jsonify({"message": f"Member with ID '{member_id}' not found"}), 404


@app.route('/update/<id>', methods=['PUT'])
def update_resource(id):
    updated_member=request.get_json()
    b=False
    for member in members_data:
        if member["id"]==id:
            for key in member.keys():
                member[key]=updated_member[key]
            b=True
    if b==False:
        return "Invalid request!", 400
    return "Resource updated successfully!", 200


@app.route('/new_member/<id>', methods=['POST'])
def post_new_member(id):
    new_member=request.get_json()
    for member in members_data:
        if id==member["id"]:
            return "Member Already Exists!!", 400
    members_data.append(new_member)
    return "New member added successfully!!", 201



if __name__ == "__main__":
    app.run(debug=True)
