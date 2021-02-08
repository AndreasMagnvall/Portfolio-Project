
# function used to create a new project from filled in template in the project file
def new_project(template):

    return {"project_id":template["project_id"],"course_id":template["course_id"],project_name:template["project_name"],"start_date":template["start_date"],
    "end_date":template["end_date"], "short_desc":template["short_desc"],long_description:template["long_description"],
    "group_size":template["group_size"],"techniques_used":template["techniques_used"],"external_link":template["external_link"],
    "big_image":template["big_image"],"small_image":template["small_image"],extra_images:template["extra_images"] }
