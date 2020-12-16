<div align="center" markdown>
<img src="https://i.imgur.com/VQSbsqa.png"/>

# Classes Co-Occurrence Matrix

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/diff-merge-project-meta)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/diff-merge-project-meta)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/diff-merge-project-meta&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/diff-merge-project-meta&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/diff-merge-project-meta&counter=runs&label=runs)](https://supervise.ly)

</div>

## Overview

Visually compare projects meta: tags and classes. Define how to merge them and how to resolve conflicts. New empty project will be created with merged classes and tags. Then you can use `Diff Merge Projects` app to merge images and annotations and place them to the project created by this application.

<img src="https://i.imgur.com/qjCJL5F.png"/>

## How To Use

**Step 1:** Add app to your team from Ecosystem if it is not there

**Step 2:** Run app from the `Apps` page of current team

<img src="https://i.imgur.com/QRYME1U.png" width="500px"/>

**Step 3:** Wait until the app is started, press `Open` button in `Workspace tasks`. You don't need to wait untill all images are processed: if open button is enabled then click it.

<img src="https://i.imgur.com/INasHFk.png"/>


**Step 4:** Explore you data with interactive table: click on cells to access corresponding images and open them in labeling UI.

**Step 5:** App saves link to report to team files: `/reports/classes-co-occurrence/<project id>_<project_name>.lnk`. Link to generated report also available in task output column. 

**Step 6:** Stop application once you finished with it. App can be stopped from tasks list or from application UI.

Example of the results:
Stop from App UI  |  Stop from workspace tasks page
:-------------------------:|:-----------------------------------:
![](https://i.imgur.com/92gkvBy.png)  |  ![](https://i.imgur.com/EzLGXdd.png)
