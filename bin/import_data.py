import xlrd
import manager_db as db

def import_data(file_data, db_file, col_name, col_email):
    wb = xlrd.open_workbook(file_data)
    n = range(wb.sheet_by_index (0).nrows)
    db.create_connection(db_file)
    db.create_table_db(db_file)
    
    ent = -1
    for i in n:
        ent = i 

    for i in n:
        if i != 0:
            data_line = (wb.sheet_by_index (0).row_values(i))      
            value = (data_line[col_name], data_line[col_email])
            #Verificar correção do códico para insersão de multiplas linhas simultaneas
            if i == 1:
                data = []
            data = data + [value]
            if (i%200 == 0) or (i == ent):
                db.insert_mult_values('data/data.db', data)
                data=[]
