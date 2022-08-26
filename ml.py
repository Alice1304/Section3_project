import sqlite3
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///cancer.db')

df = pd.read_sql('SELECT * FROM cancer',engine)

c_t = df.copy()

c_t = c_t.dropna(subset=['statsTrgtNm'])

c_t.replace({'ptSexCd' : {'F' : 1, 'M': 2},
            'statsTrgtNm' : {'무직' : 1, '회사원' : 2, '기타' : 3, '자유업' : 4, '전문직' :5, '교사' :6, '학생' : 7, '군인' :8, '주부' : 9, '무응답' : 10 }}, inplace = True
)

###머신러닝 모델 돌리기 

#필요한 인스톨 설치
#pip install scikit-learn
#pip3 install numpy

#트레인 테스트 스플릿 
from sklearn.model_selection import train_test_split
train, test = train_test_split(c_t, random_state=2)

target = 'type'
features = ['ptAge','ptSexCd','statsTrgtNm']

X_train = train[features]
y_train = train[target]
X_test = test[features] 
y_test = test[target]

#모델인스턴스만들기 
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

#학습하기
model.fit(X_train, y_train)


X_test = [[27, 1, 3]]
y_pred = model.predict(X_test)



###피클링하기 
import pickle

with open('model.pkl', 'wb') as pickle_file:
    pickle.dump(model, pickle_file)