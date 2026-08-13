Students = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}



def promedioValoresDiccionario(ages):
    length = len(ages)
    return(sum(ages.values()) / length)

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

print(promedioValoresDiccionario(ages))


def oldestStudent(ages):
    value = list(ages.values())
    key = list(ages.keys())
    return key[value.index (max(value))]
print("nombre del estudiante más viejo:", oldestStudent(ages))


def updateAges(ages, n):
    new_ages = {}
    for word in ages:
        new_ages[word] = ages[word] + n
    return new_ages

print("edades actualizadas:", updateAges(ages, 1))


def totalStudents(students):
    return (len(students.keys()))

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(totalStudents(students))


def calculateAverageAge(students):
    result = {}
    add_age = 0
    for thing in students.values():
        age = thing['age']
        add_age = add_age + age
        
    return(add_age / len(students.keys()))    

def find_students(address, students):
    names = []
    for key, subdict in students.items():
        for sublist in subdict.values():
            if (sublist == address):
                names.append(key)
                
    return sorted(names)