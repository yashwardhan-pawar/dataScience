import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from fifa19 import StringBuilder
from fifa19 import IntegerUtility
from fifa19 import DBConnection
import sys
iu = IntegerUtility.MyClass();

def insert(detailed_columns, detailed_data):
    connect = DBConnection.dbConnect();
    for index, row in detailed_data.iterrows():
#         insertData(mycursor, detailed_columns,detailed_data.loc[detailed_data["ID"] == index], "football_player_details")
#        insertData(mycursor, detailed_columns, row, "football_player_details")
        insertData(connect, detailed_columns, detailed_data.iloc[index], "football_player_details")
    connect.dbDisconnect();

    
def safe_str(obj):
    try:
        val = str(obj)
        if val != "nan":
            if iu.isInt(obj):
                return str(obj)
            else:
                return "\"" + str(obj) + "\""
        else:
            return "NULL"
    except:
#         print(type(obj))
        return "NULL"

def createDbTable(cursor, columnNames, datarow, tableName):
    sqlCols = StringBuilder.AppendString("CREATE TABLE DATA_SCIENCE." + tableName + " (")
    for cols in columnNames:
        val = datarow.get(cols).values[0]
        sqlCols.append(cols.replace(" ", "_") + (" VARCHAR(256), ", " INTEGER(32), ")[iu.isInt(val)])
    sqlCols.removeTrailingChar(2)
    sqlCols.append(")")
#     print(sqlCols.toString())
    cursor.execute(sqlCols.toString())


def insertData(connect, columnNames, dataToInsert, tableName):
#     deleteSql = "delete from DATA_SCIENCE.football_player_data where PID = "+dataToInsert.get("ID").values[0]
#     connect.executeQuery(deleteSql);

    # insertSql = "insert into DATA_SCIENCE.football_player_data values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    insertVal = StringBuilder.AppendString("insert into DATA_SCIENCE." + tableName + " values (")
    
    for cols in columnNames:
#         val = dataToInsert.get(cols).values[0]

        if not isinstance(dataToInsert, tuple):
            val = dataToInsert.get(cols)
        else:
            val = dataToInsert.get(cols).values[0]
        val = safe_str(val)
        insertVal.append(val + ", ")
    insertVal.removeTrailingChar(2)
    insertVal.append(")")
#     print(insertVal.toString())
    connect.executeQuery(insertVal.toString())


def playerData(insertFlag, createFlag):
    # Get basic players informaticon for all players
    if insertFlag or createFlag : 
            connect = DBConnection.dbConnect();
            mycursor = connect.dbCusror()
        
    base_url = "https://sofifa.com/players?offset="
    columns = ['ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Special']
    data = pd.DataFrame(columns=columns)
    for offset in range(290, 300):
        url = base_url + str(offset * 61)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        table_body = soup.find('tbody')
        for row in table_body.findAll('tr'):
            td = row.findAll('td')
            picture = td[0].find('img').get('data-src')
            pid = td[0].find('img').get('id')
            nationality = td[1].find('a').get('title')
            flag_img = td[1].find('img').get('data-src')
            name = td[1].findAll('a')[1].text
            age = td[2].find('div').text.strip()
            overall = td[3].text.strip()
            potential = td[4].text.strip()
            club = td[5].find('a').text
            club_logo = td[5].find('img').get('data-src')
            value = td[6].text.strip()
            wage = td[7].text.strip()
            special = td[8].text.strip()
            player_data = pd.DataFrame([[pid, name, age, picture, nationality, flag_img, overall, potential, club, club_logo, value, wage, special]])
            player_data.columns = columns
            data = data.append(player_data, ignore_index=True)
#             print(pid)
            if createFlag:
                createDbTable(mycursor, columns, data, "football_player_data")
                createFlag = False
            if insertFlag:
                insertData(connect, columns, player_data, "football_player_data")
        print("Adding data for Page: " + str(offset))
    data = data.drop_duplicates()
    
    if connect.isOpen():
        connect().dbDisconnect()
    print(data)
    return data

# Get detailed player information from player page
def playerDetails(insertFlag, createFlag):
    connect = DBConnection.dbConnect();
    mycursor = connect.dbCusror()
    mycursor.execute("SELECT D.* FROM DATA_SCIENCE.football_player_data D WHERE D.PID NOT IN ( SELECT PID FROM DATA_SCIENCE.football_player_details) LIMIT 250")
    data = mycursor.fetchall()
    connect.dbDisconnect;
    
    detailed_columns = ['Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'ID']
#     print("Rows to be inserted: "+str(len(data)))
    detailed_data = pd.DataFrame(index=range(0, len(data)), columns=detailed_columns)
    detailed_data.ID = list(zip(*data))[0]
    print("Fetching Data."),
    player_data_url = 'https://sofifa.com/player/'
    for id in detailed_data.ID:
        url = player_data_url + str(id)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        skill_map = {}
        columns = soup.find('div', {'class': 'teams'}).find('div', {'class': 'columns'}).findAll('div', {'class': 'column col-4'})
        for column in columns:
            skills = column.findAll('li')
            for skill in skills:
                if(skill.find('label') != None):
                    label = skill.find('label').text
                    value = skill.text.replace(label, '').strip()
                    skill_map[label] = value
        meta_data = soup.find('div', {'class': 'meta'}).text.split(' ')
        length = len(meta_data)
        weight = meta_data[length - 1]
        height = meta_data[length - 2].split('\'')[0] + '\'' + meta_data[length - 2].split('\'')[1].split('\"')[0]
        skill_map["Height"] = height
        skill_map['Weight'] = weight
        if('Position' in skill_map.keys()):
            if skill_map['Position'] in ('', 'RES', 'SUB'):
                skill_map['Position'] = soup.find('article').find('div', {'class': 'meta'}).find('span').text
            if(skill_map['Position'] != 'GK'):
                card_rows = soup.find('aside').find('div', {'class': 'card mb-2'}).find('div', {'class': 'card-body'}).findAll('div', {'class': 'columns'})
                for c_row in card_rows:
                    attributes = c_row.findAll('div', {'class': re.compile('column col-sm-2 text-center')})
                    for attribute in attributes:
                        if(attribute.find('div')):
                            name = ''.join(re.findall('[a-zA-Z]', attribute.text))
                            value = attribute.text.replace(name, '').strip()
                            skill_map[str(name)] = value
        sections = soup.find('article').findAll('div', {'class': 'mb-2'})[1:3]
        first = sections[0].findAll('div', {'class': 'column col-4'})
        second = sections[1].findAll('div', {'class': 'column col-4'})[:-1]
        sections = first + second
        for section in sections:
            items = section.find('ul').findAll('li')
            for item in items:
                value = int(re.findall(r'\d+', item.text)[0])
                name = ''.join(re.findall('[a-zA-Z]*', item.text))
                skill_map[str(name)] = value
        for key, value in skill_map.items():
            detailed_data.loc[detailed_data.ID == id, key] = value
        if createFlag:
            createDbTable(mycursor, detailed_columns, detailed_data, "football_player_details")
            createFlag = False
        if insertFlag:
            insertData(mycursor, detailed_columns, detailed_data.loc[detailed_data["ID"] == id], "football_player_details")
        print("."),
    return detailed_data



# playerData(True, False)
# sys.exit(0)
detailed_columns = ['Preferred Foot', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position', 'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until', 'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'ID']
columns = ['ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag', 'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Special']

i = 99;
while i<75:
    detailed_data = playerDetails(False, False)
    insert(detailed_columns, detailed_data)
    i += 1
    print("Total Inserted: " + str(i * len(detailed_data)))

connect = DBConnection.dbConnect();
mycursor = connect.dbCusror()
mycursor.execute("SELECT * FROM DATA_SCIENCE.football_player_data")
data = mycursor.fetchall()

mycursor.execute("SELECT * FROM DATA_SCIENCE.football_player_details")
details = mycursor.fetchall()
connect.dbDisconnect;


player_data = pd.DataFrame(data, columns=columns)
player_detail = pd.DataFrame(details, columns=detailed_columns)


full_data = pd.merge(player_data, player_detail, how = 'inner', on = 'ID')
full_data.to_csv('fifa19data.csv', encoding='utf-8')
print("End")

