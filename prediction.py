class asdf:
    def __init__(self):

df_krx = fdr.StockListing('KRX')
df_naver = fdr.DataReader('005930', '2018')

target = df_naver['Close']
pred = df_naver[['Open']]

x_train, x_test, y_train, y_test = train_test_split(pred, target, test_size = 0.3, random_state = 25, shuffle=False)

randomforest = RandomForestRegressor(random_state=0)
randomforest.fit(x_train, y_train)
y_pred_rf = randomforest.predict(x_test)