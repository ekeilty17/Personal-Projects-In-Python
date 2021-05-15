from mysql import *

if __name__ == '__main__':
    # Init
    db = Database('localhost', 'eric', 'eric', 'python')
    db.reset()

    """
    # MANUAL TEST
    # Creating Table
    db.add_table('test')
    
    # Creating Columns
    db.add_column('test', 'name', 'string', False)
    db.add_column('test', 'description', 'string', True)
    db.add_column('test','age', 'int', False)
    db.add_column('test','isSmart', 'boolean', True)
    
    # Getting Column Names
    print()
    print("Column Names:")
    print(db.get_all_columns('test'))
    print()

    # Populating
    A = ["Eric", "UofT Engineering Science Student", 19 , True]
    db.add_data('test', A)
    A = ["Nicole", "UofT Civil Engineering Student", 18, True]
    db.add_data('test', A)
    A = ["Matt", "Dover Highschool Student", 17, False]
    db.add_data('test', A)
    
    # Getting
    db.get_all_data('test')
    db.get_specific_columns('test', ["name", "age"])
    
    # Filtering
    db.filter_data('test', "name = 'Matt' OR isSmart = 1")
    """

    """
    # JSON TEST
    # Creating Table
    db.add_table('test')

    # Populating
    J = json.loads('{"name" : "Eric" , "description" : "UofT Engineering Science Student" , "age" : 19 , "isSmart" : true}')
    db.add_data_json('test', J)
    J = json.loads('{"isSmart" : true , "name" : "Nicole" , "description" : "UofT Civil Engineering Student" , "age" : 18}')
    db.add_data_json('test', J)
    J = json.loads('{"name" : "Matt" , "description" : "Dover Highschool Student" , "age" : 17 , "isSmart" : false}')
    db.add_data_json('test', J)

    # Getting
    db.get_all_data('test')
    """

    # JSON File TEST
    # Creating Table
    db.add_table('test')

    # Populating
    db.load_json('test','data.json')

    # Getting
    db.get_all_data('test')
