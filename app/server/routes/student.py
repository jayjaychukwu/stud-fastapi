from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()


@router.post("/", response_description="student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, 201, "student added successfully")


@router.get("/", response_description="students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, 200, "students data retrieved successfully")
    return ResponseModel(students, 200, "empty list returned")


@router.get("/{id}", response_description="student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, 200, "student data retrieved successfully")
    return ErrorResponseModel("an error occured", 404, "student does not exist")


@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "student with ID: {} update is successful".format(id), 200, "student data updated successfully"
        )
    return ErrorResponseModel(
        "an error occured",
        404,
        "there was an error updating the student data",
    )


@router.delete("/{id}", response_description="student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            f"student with ID: {id} has been removed",
            200,
            "student deleted successfully",
        )
    return ErrorResponseModel(
        "an error occured",
        404,
        f"student with ID {id} does not exist",
    )
