class Patient:
    __patient_count = 0
 
    def __init__(self, patient_id, name, disease, doctor):
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__doctor = doctor
        Patient.__patient_count += 1
 
    def display(self):
        print("Patient ID:", self.__patient_id)
        print("Name:", self.__name)
        print("Disease:", self.__disease)
        print("Doctor:", self.__doctor)
 
    def change_doctor(self, new_doctor):
        if new_doctor != "":
            self.__doctor = new_doctor
            print("Doctor changed")
        else:
            print("Invalid doctor name")
 
    @classmethod
    def from_string(cls, details):
        patient_id, name, disease, doctor = details.split("-")
        return cls(int(patient_id), name, disease, doctor)
 
    @classmethod
    def get_patient_count(cls):
        return cls.__patient_count
 
 
p1 = Patient.from_string("201-Aman-Fever-Dr Sharma")
p1.display()
p1.change_doctor("Dr Khan")
p1.display()
print("Total patients:", Patient.get_patient_count())
