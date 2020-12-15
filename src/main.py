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


@my_app.callback("merge")
@sly.timeit
def merge(api: sly.Api, task_id, context, state, app_logger):
    pass


def init_ui(api: sly.Api, task_id, app_logger):
    global PROJECT1, PROJECT2, META1, META2

    PROJECT1 = api.project.get_info_by_id(PROJECT_ID1)
    PROJECT2 = api.project.get_info_by_id(PROJECT_ID2)

    META1 = sly.ProjectMeta.from_json(api.project.get_meta(PROJECT_ID1))
    META2 = sly.ProjectMeta.from_json(api.project.get_meta(PROJECT_ID2))

    classes1 = {obj_class.name: obj_class.geometry_type for obj_class in META1.obj_classes}
    classes2 = {obj_class.name: obj_class.geometry_type for obj_class in META2.obj_classes}

    mutual_classes = classes1.keys() & classes2.keys()
    diff_classes1 = classes1.keys() - mutual_classes
    diff_classes2 = classes2.keys() - mutual_classes


    for class_name in mutual_classes:



    data = {
        "projectId1": PROJECT1.id,
        "projectName1": PROJECT1.name,
        "projectPreviewUrl1": api.image.preview_url(PROJECT1.reference_image_url, 100, 100),
        "projectId2": PROJECT2.id,
        "projectName2": PROJECT2.name,
        "projectPreviewUrl2": api.image.preview_url(PROJECT2.reference_image_url, 100, 100)
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