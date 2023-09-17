from flask_restx import Namespace, Resource
from flask import request
import functions.mongodb as mongodb
import functions.utils as utils


api = Namespace('mongodb crud', description='Mongo related operations')

@api.route("/<coll_name>")
class curds(Resource):
    def get(self, coll_name):
        documents = mongodb.all_documents(coll_name)
        return utils.send_json(documents)
    
    def post(self, coll_name):
        inserted_document = mongodb.insert_document(coll_name, request.json)
        report_id = str(inserted_document.inserted_id)
        return utils.send_json({"msg": f"{coll_name} entry succefully saved in db.", "inserted_id": report_id})
    
@api.route("<coll_name>/id/<id>")
class curd(Resource):
    def get(self, coll_name, id):
        document = mongodb.find_document(coll_name, id)
        return utils.send_json(document) if ( (isinstance(document, dict)) and (len(document) != 0) ) else utils.send_json({})
    
    def delete(self, coll_name, id):
        deleted_doc = mongodb.delete_decument(coll_name, id)
        msg = "document succesfully deleted" if deleted_doc.deleted_count == 1 else "no document found for deletion"
        return utils.send_json({"msg": msg})
    
    def put(self, coll_name, id):
        body = request.get_json(force=True, silent=True)
        update = utils.check_body(body)
        if (len(update) == 0):
            return utils.send_json({"status": "fail", "msg": "update query empty, please provide non empty json object"})
        updated_doc = mongodb.update_document(coll_name, id, update)
        msg = ""
        if updated_doc.matched_count == 0:
            msg = "no document found for update"
        else:
            msg = "document succesfully updated" if updated_doc.modified_count == 1 else "document found but no modifications done"
        return utils.send_json({"msg": msg})
