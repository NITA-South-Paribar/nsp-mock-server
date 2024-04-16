from flask import Flask, jsonify
import json


app = Flask(__name__)

members_data = json.load(open('nsp_members.json','r'))

@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members_data)


@app.route("/members/<member_id>", methods=["GET"])
def get_member(member_id):
    for member in members_data:
        if member["id"] == member_id:
            return jsonify(member)
    return jsonify({"message": f"Member with ID '{member_id}' not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
