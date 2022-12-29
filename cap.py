import pyodbc
conn = pyodbc.connect('Driver={SQLServer};'
                      'Server=HCL-02-19\SQLEXPRESS;'
                      'Database=FileSearchResults;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
                 INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                 VALUES
                 ('E:\project_1\harisree.txt'),
                 ('E:\project_1\project_2\harisree.txt')
                 ''')
conn.commit();
cursor.execute('Select * From FileSearchResults_table')
File_input = 'harikasree_file.txt'