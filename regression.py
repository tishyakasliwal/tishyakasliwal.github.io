import turicreate
sf=turicreate.SFrame("noida data.csv")

features=['Sector','Crime','Population']
train_data,test_data = sf.random_split(.8,seed=0)

#predicitng the safety index
model=turicreate.linear_regression.create(train_data,target='Crime level', features=features, validation_set=None)
predictions=model.predict(test_data)


print(model.evaluate(test_data))

