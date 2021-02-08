import json
import copy

#return the text in the json file in the list format
def load(filename):
    ids = []
    with open(filename, 'r') as file:
        db = json.load(file)

        if type(db) == list:
            for project in db:
                if "project_id" in project.keys():
                    ids.append(project["project_id"])
            print(len(ids))
            print(len(set(ids)))
            if len(ids) > len(set(ids)):
                raise Exception('Multiple projects with same id in database!')

        return db


#return the amount of projects in the database
def get_project_count(db):
    return len(db)

#returns the project with the specified id
def get_project(db, id):
    for project_index in range(0, len(db)):
        if db[project_index]["project_id"] == id:
            return db[project_index]
    return None

#returns a list of of all keys from all projects, skipping doubletts
def get_keys(db):
    keys = []
    for project in db:
        for key in project.keys():
            keys.append(key)

    return list(set(keys))

#returns a list of the projects that match the arguments techniques and search
def filter_list(db, techniques, search, search_fields):
    project_list = []
    project_list[:] = copy.deepcopy(db)

    #removes projects not using the specified techniques
    if techniques != None:
        for tech_index in range(0, len(techniques)):
            project_list = list(filter(lambda x: techniques[tech_index] in x["techniques_used"], project_list))

    #removes projects if the searched word can not be found
    if search != None:
        for project_index in reversed(range(0, len(project_list))):
            if search_fields == None:
                key_list = list(project_list[project_index].keys())
                for key_index in reversed(range(0, len(key_list))):
                    # all projects might not have the same key, verify beforehand to avoid crash
                    if key_list[key_index] in project_list[project_index]:
                        if search.lower() in str(project_list[project_index][key_list[key_index]]).lower():
                            break
                    if key_index == 0:
                        project_list.pop(project_index)
                        break
            else:
                for key_index in reversed(range(0, len(search_fields))):
                    # all projects might not have the same key, verify beforehand to avoid crash
                    if search_fields[key_index] in project_list[project_index]:
                        if search.lower() in str(project_list[project_index][search_fields[key_index]]).lower():
                            break
                    if key_index == 0:
                        project_list.pop(project_index)
                        break

    return project_list

#returns a sorted list of projects matching the arguments techniques and search
def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):

    #if there is a search argument but an empty list in the search_fields argument, return an empty list instead
    if search and search_fields == []:
        return []

    project_list = filter_list(db, techniques, search, search_fields)

    if sort_order == 'desc':
        list.sort(project_list, key = lambda x: x[sort_by], reverse=True)
    else:
        list.sort(project_list, key = lambda x: x[sort_by], reverse=False)
    return project_list

#returns a list of techniques found in all projects
def get_techniques(db):
    techs = set([])

    for project in db:
        for tech in project["techniques_used"]:
             techs.add(tech)

    techs = list(techs)
    list.sort(techs)

    return techs

#returns a list of the id and names of all projects ordered after techniques
def get_technique_stats(db):
    tech_set = get_techniques(db)
    tech_stats = dict.fromkeys(tech_set, [])

    for tech in tech_stats:
        test_list = []
        for project in db:
            if tech in project["techniques_used"]:
                test_list.append({'id':project["project_id"], 'name':project["project_name"]})
                tech_stats[tech] = test_list

    return tech_stats

#retuns some part of the user info for the project page
def get_user_info(db,key):
    return load(file)[0][key]
