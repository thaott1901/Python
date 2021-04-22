import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

train_data = pd.read_csv("train.csv")
train_data.head()

test_data = pd.read_csv("test.csv")
test_data.head()

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

imputer = SimpleImputer()
X_imputed =  pd.DataFrame(imputer.fit_transform(X))
X_imputed.columns = X.columns

model = RandomForestClassifier(n_estimators=300,max_depth=10,random_state=1)
model.fit(X_imputed,y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId,'Survived': predictions})
output.to_csv('my_submission_v01.csv', index=False)
print("Your submission was successfully saved!")