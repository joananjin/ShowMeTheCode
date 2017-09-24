import mysql.connector
from mysql.connector import errorcode
from random import Random


def random_codes(n):
    random_length = 20
    codes = []
    random = Random()
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(n):
        code = ''
        for j in range(random_length):
            code += chars[random.randint(0, len(chars) - 1)]
        codes.append(code)
    return codes


if __name__ == '__main__':
    codes = random_codes(200)
    cnx = mysql.connector.connect(user="root", password="123456", host="localhost", database="python")
    cursor = cnx.cursor()
    drop_table = (
        '''
        drop table if EXISTS active_codes;
        '''
    )
    cursor.execute(drop_table)

    create_table = (
        """
        CREATE TABLE if NOt EXISTS active_codes (
          id int(11) NOT NULL,
          codes VARCHAR(20) NOT NULL,
          PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """)

    add_active_codes=(
        """
        INSERT INTO active_codes
        VALUES (%s, %s)
        """
    )

    # for result in cursor.execute(create_table, multi=True):
    #     pass

    cursor.execute(create_table)


    for i in range(len(codes)):
        data_active_codes = (i+1, codes[i])
        cursor.execute(add_active_codes, data_active_codes)
    #
    #
    #
    cnx.commit()
    cursor.close()
    cnx.close()
