import sqlite3


def add_pet(body):  # noqa: E501
    conn = sqlite3.connect('../base.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO pets (id, name, age) VALUES(' + str(body["id"]) + ", '"+ body["name"] + "', " + str(body["age"]) + ")")
    conn.commit()
    cur.close()
    return


def get_all_pets():  # noqa: E501
    conn = sqlite3.connect('../base.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM pets;')
    pets = cur.fetchall()
    cur.close()
    for pet in pets:
        print(f'id={pet[0]} name={pet[1]} age={pet[2]}')
    return


def get_pet_by_id(petId):  # noqa: E501
    conn = sqlite3.connect('../base.db')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM pets WHERE id={petId};')
    pets = cur.fetchall()
    cur.close()
    for pet in pets:
        print(f'id={pet[0]} name={pet[1]} age={pet[2]}')
    return
