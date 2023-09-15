from flask_restx import Namespace, Resource
from flask import request
import functions.mongodb as mongodb
import functions.utils as utils

api = Namespace('experiences', description='Experiences related operations')

@api.route("/")
class experiences(Resource):
    def get(self):
        documents = mongodb.all_documents("experiences")
        return utils.send_json(documents)
    
    def post(self):
        inserted_document = mongodb.insert_document("experiences", request.json)
        report_id = str(inserted_document.inserted_id)
        return utils.send_json({"msg": "experience entry succefully saved in db.", "inserted_id": report_id})
    
@api.route("/id/<id>")
class experience(Resource):
    def get(self, id):
        document = mongodb.find_document("experiences", id)
        return utils.send_json(document) if ( (isinstance(document, dict)) and (len(document) != 0) ) else utils.send_json({})
    
    def delete(self, id):
        deleted_doc = mongodb.delete_decument("experiences", id)
        msg = "document succesfully deleted" if deleted_doc.deleted_count == 1 else "no document found for deletion"
        return utils.send_json({"msg": msg})
    
    def put(self, id):
        body = request.get_json(force=True, silent=True)
        update = utils.check_body(body)
        if (len(update) == 0):
            return utils.send_json({"status": "fail", "msg": "update query empty, please provide non empty json object"})
        updated_doc = mongodb.update_document("experiences", id, update)
        msg = ""
        if updated_doc.matched_count == 0:
            msg = "no document found for update"
        else:
            msg = "document succesfully updated" if updated_doc.modified_count == 1 else "document found but no modifications done"
        return utils.send_json({"msg": msg})
