from db import db
import pymongo
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder


class CRUD:
    def __init__(self):
        self.students = db["students"]
        self.counter_collection = db["counters"]

    def get_next_sequence_value(self, sequence_name):
        counter = self.counter_collection.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"sequence_value": 1}},
            upsert=True,
            return_document=pymongo.ReturnDocument.AFTER,
        )
        return counter["sequence_value"]

    def create(self, student):
        try:
            student = jsonable_encoder(student)
            student_id = self.get_next_sequence_value("student_id")
            student["id"] = student_id
            db.students.insert_one(student)
            return {"id": student_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def list(self, country, age):
        try:
            response = list(
                self.students.find(
                    {"address.country": country, "age": {"$gte": age}},
                    {"_id": 0, "name": 1, "age": 1},
                )
            )
            return {"data": response}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def fetch(self, id):
        try:
            response = self.students.find_one({"id": id}, {"_id": 0, "id": 0})
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update(self, id, updates):
        try:
            updates = jsonable_encoder(updates)
            updates = {
                key: value for key, value in updates.items() if value is not None
            }
            if not updates:
                raise HTTPException(
                    status_code=400, detail="No fields provided for update"
                )

            self.students.update_one({"id": id}, {"$set": updates})
            return {}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete(self, id):
        try:
            data = self.students.find_one({"id": id})
            if data:
                raise HTTPException(status_code=400, detail="No student found")
            self.students.delete_one({"id": id})
            return {}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


crud = CRUD()
