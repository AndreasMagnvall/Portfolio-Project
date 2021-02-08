import project
import user


user_info = user.new_user(header1 = "EN COOL RUBRIK",header2 = "EN inte lika cool rubrik",text1= "Jag gillar minecraft",text2 = "Men inte latex",bigimage = "finbild.png",links = ["github.com"])
#writes new data to the json data file
def add_to_db(data):
    db = load("data.json")
    db.append(data)
    with open('data.json', 'w') as file:
        json.dump(db, file, indent=4)

def change_user_info(data):
    with open('user.json', 'w') as file:
        json.dump(data, file, indent=4)

#edit this to add a new project and uncomment add_to_db(project_temp), run the file, the recomment the same line
project_temp = {
"start_date": "2009-09-07",
"short_description": "no",
"course_name": "HOHO",
"long_description": "no no no",
"group_size": 8,
"academic_credits": "WUT?",
"external_link": "YY",
"small_image": "X",
"techniques_used": ["css","html"

],
"project_name": ",",
"course_id": " \"",
"end_date": "2009-09-07",
"project_id": 4,
"big_image": "XXX"
}

#
#add_to_db(project_temp)
#

#change_user_info(user_info)
