from Domain.student_validator import StudentValidator
from Repository.student_repository import StudentRepository
from Repository.student_repository_file import StudentRepositoryFile
from Service.student_service import StudentService
from Userinterface.console import Userinterface

# student_repository = StudentRepository()
# student_validator = StudentValidator()
# student_service = StudentService(student_repository, student_validator)
# console = Userinterface(student_service)

student_repository_fisier = StudentRepositoryFile("studenti.txt")
validator = StudentValidator()
service = StudentService(student_repository_fisier, validator)
console = Userinterface(service)

console.program()
