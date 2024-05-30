Cogno_pluse

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://github.com/suuj3/Cogno-pulse
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://github.com/suuj3/Cogno-pulse/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)


## Name
Cogno-Pluse: AI based Personality Prediction System

## Description
Traditional personality testing systems often rely on subjective assessments and are not accurate and efficient enough to give useful insights of personality traits to users. So, there is a clear need for a more objective, data-driven method to evaluate personality traits that can leverage machine learning algorithms to enhance the reliability, accuracy, and personalization of the results.

## Visuals
User integrateion of Cogno pluse is as shown below:
![Screenshot (456)](https://github.com/suuj3/Cogno-pulse/assets/118878065/80b94189-df97-4bcf-9227-43a7ba19dd96)

After clicking the 'Let's Go' button users will be displayed with series of questions:
![Screenshot (457)](https://github.com/suuj3/Cogno-pulse/assets/118878065/a6036331-37f6-4e50-85e7-3e5676d9ba7d)
![Screenshot (458)](https://github.com/suuj3/Cogno-pulse/assets/118878065/19056388-529d-4c3a-954e-e0c62e94f363)

After answering the questions user can check their personality type:
![Screenshot (459)](https://github.com/suuj3/Cogno-pulse/assets/118878065/16d26b5d-8aea-4c70-8480-b160d43ac983)

## Usage
You should install the following libraries;
pip install flask
pip instal sklearn
pip install numpy, pandas, matplotlib

You should import the following librarie from sklearn; 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import precision_score, recall_score, confusion_matrix, f1_score,accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestClassifier

We have trained 7 different models to optimize the performance.
![Screenshot (460)](https://github.com/suuj3/Cogno-pulse/assets/118878065/1812baae-3782-40fe-b2f6-0c8426beaa82)

This is the final pipeline you will get:
![Screenshot (461)](https://github.com/suuj3/Cogno-pulse/assets/118878065/862205dd-e062-4769-a741-e018b1b0d3a1)

## Support
if you have any questions on the reach out to this email 12220083.gcit@rub.edu.bt, 12220099.gcit@rub.edu.bt, 12220101.gcit@rub.edu.bt, 12220077.gcit@rub.edu.bt

## Roadmap
For now the project has only 5 target namely Extraverted, Lively, Dependable, Responsible and Serious, In the future we can improve into big5 personality prediction where it will predict 16 personality.

## Authors and acknowledgment
This is a group project and I appreciate for every members contributions and hardwork.

## License
Everyone is free to use this source code.

## Project status
This project is a group project and is deployed in onrender.com
