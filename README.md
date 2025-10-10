<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/106374579/182864698-073d3481-628e-43f4-a074-85bf3abeae3d.png"/>

# Diff Merge Project Meta

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](../../../../supervisely-ecosystem/diff-merge-project-meta)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/diff-merge-project-meta)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/diff-merge-project-meta.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/diff-merge-project-meta.png)](https://supervisely.com)

</div>

## Overview

Visually compare projects meta: tags and classes. Define how to merge them and how to resolve conflicts. New empty project will be created with merged classes and tags. Then you can use [`Diff Merge Images Projects`](https://app.supervisely.com/ecosystem/apps/diff-merge-images-projects) app to merge images and annotations and place them to the project created by this application.

<img src="https://i.imgur.com/qjCJL5F.png"/>

## How To Use

**Step 1:** Add app to your team from Ecosystem if it is not there

**Step 2:** Run app from the `Apps` page of current team

<img src="https://i.imgur.com/QRYME1U.png" width="500px"/>

**Step 3:** Explore comparison tables, define merge options and press `Run` button.

**Step 4:** New project is created. Information about input projects is saved in `custom data` of created project. For example:

```json
{
  "project1": {
    "id": 1436,
    "name": "lemons_annotated"
  },
  "project2": {
    "id": 1455,
    "name": "kiwi_annotated"
  }
}
```

<img src="https://i.imgur.com/TR070VM.png"/>

**Step 5:** Task is created in `Application Sessions`. 
