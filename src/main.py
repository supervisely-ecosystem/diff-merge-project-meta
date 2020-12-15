import os
import supervisely_lib as sly


my_app = sly.AppService()

TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])

PROJECT_ID1 = int(os.environ['modal.state.projectId1'])
PROJECT1 = None
META1 = None

PROJECT_ID2 = int(os.environ['modal.state.projectId2'])
PROJECT2 = None
META2 = None


def process_items(collection1, collection2, diff_msg="Shapes differ"):
    items1 = {item.name: 1 for item in collection1}
    items2 = {item.name: 1 for item in collection2}
    names = items1.keys() | items2.keys()
    mutual = items1.keys() & items2.keys()
    diff1 = items1.keys() - mutual
    diff2 = items2.keys() - mutual

    match = []
    differ = []
    missed = []

    def set_info(d, index, meta):
        d[f"class{index}"] = meta.name
        d[f"color{index}"] = sly.color.rgb2hex(meta.color)
        if type(meta) is sly.ObjClass:
            d[f"shape{index}"] = meta.geometry_type.geometry_name()
            d[f"shapeIcon{index}"] = "zmdi zmdi-shape"
        else:
            meta: sly.TagMeta
            d[f"shape{index}"] = meta.value_type
            d[f"shapeIcon{index}"] = "zmdi zmdi-label"

    for name in names:
        compare = {}
        meta1 = collection1.get(name)
        if meta1 is not None:
            set_info(compare, 1, meta1)
        meta2 = collection2.get(name)
        if meta2 is not None:
            set_info(compare, 2, meta2)

        compare["infoMessage"] = "Match"
        compare["infoColor"] = "green"
        if name in mutual:
            flag = True
            if type(meta1) is sly.ObjClass and meta1.geometry_type != meta2.geometry_type:
                flag = False
            if type(meta1) is sly.TagMeta and meta1.value_type != meta2.value_type:
                flag = False

            if flag is False:
                compare["infoMessage"] = diff_msg
                compare["infoColor"] = "red"
                compare["infoIcon"] = ["zmdi zmdi-close"],
                differ.append(compare)
            else:
                compare["infoIcon"] = ["zmdi zmdi-check"],
                match.append(compare)
        else:
            if name in diff1:
                compare["infoMessage"] = "Missing in Project #2"
                compare["infoIcon"] = ["zmdi zmdi-alert-circle-o", "zmdi zmdi-long-arrow-right"]
                compare["iconPosition"] = "right"
            else:
                compare["infoMessage"] = "Missing in Project #1"
                compare["infoIcon"] = ["zmdi zmdi-long-arrow-left", "zmdi zmdi-alert-circle-o"]
            compare["infoColor"] = "#FFBF00"
            missed.append(compare)

    table = []
    table.extend(match)
    table.extend(differ)
    table.extend(missed)
    return table


def init_ui(api: sly.Api, task_id, app_logger):
    global PROJECT1, PROJECT2, META1, META2

    PROJECT1 = api.project.get_info_by_id(PROJECT_ID1)
    PROJECT2 = api.project.get_info_by_id(PROJECT_ID2)

    if PROJECT1.type != PROJECT2.type:
        raise TypeError(f"Projects have different types: {str(PROJECT1.type)} != {str(PROJECT2.type)}")

    META1 = sly.ProjectMeta.from_json(api.project.get_meta(PROJECT_ID1))
    META2 = sly.ProjectMeta.from_json(api.project.get_meta(PROJECT_ID2))

    classes_table = process_items(META1.obj_classes, META2.obj_classes)
    tags_table = process_items(META1.tag_metas, META2.tag_metas, diff_msg="Tag type differ")

    data = {
        "projectId1": PROJECT1.id,
        "projectName1": PROJECT1.name,
        "projectPreviewUrl1": api.image.preview_url(PROJECT1.reference_image_url, 100, 100),
        "projectId2": PROJECT2.id,
        "projectName2": PROJECT2.name,
        "projectPreviewUrl2": api.image.preview_url(PROJECT2.reference_image_url, 100, 100),
        "cards": [
            {
                "table": classes_table,
                "name": "Compare Classes",
                "description": "Classes colors are ignored",
                "columnSuffix": "classes"
            },
            {
                "table": tags_table,
                "name": "Compare Tags",
                "description": "Tags colors are ignored",
                "columnSuffix": "tags"
            }
        ]
    }
    state = {
    }

    return data, state


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": TEAM_ID,
        "WORKSPACE_ID": WORKSPACE_ID,
    })

    data, state = init_ui(my_app.public_api, my_app.task_id, my_app.logger)
    my_app.run(data=data, state=state, initial_events=[{"command": "compare"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)