# Overview

A place to document our use cases for Data Object Service (DOS).

## Presentation wtih an Overview

https://docs.google.com/presentation/d/18vB5wDvvvW4nlZDtbidcY5Sv5TbbegLRTT2Ar1a38-U/edit#slide=id.g1cffa4d16d_15_0

## Google Doc with Use Cases

https://docs.google.com/document/d/1KNKYhMLzzbbS4x79PZE_GgVPaPSa4zNpZiey4fF1-Vo/edit

## Cromwell

The Cromwell group has 4 instances via 2 projects where DOS is being considered. These are all similar enough to effectively be a single use case. We need to model an institution's local storage as a private cloud exposing basic read/write/sizeof functionality akin to GCS or S3. For instance instead of `gs:this/is/my/bucket` it'd be `site1:this/is/my/bucket` or `site2:this/is/my/bucket`. While these use cases don't *need* human readability the stakeholders have expressed preferences towards this over UUID approaches. Similar stances have been taken regarding putting a redirection utility in front of these private clouds.

## Pull Request in Schemas' Repo

This is work Brian Walsh at OHSU and others have contributed.  Would be nice to sub-module this here.  Needs discussion, please comment on the pull request.

https://github.com/ga4gh/ga4gh-schemas/pull/874
