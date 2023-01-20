#まずは、Streamlitをインストールします
pip install streamlit

#次に、最適化問題を設定します。以下は、例として、運賃の最小化問題を設定した例です。

from scipy.optimize import minimize

def fare_optimization(x):
    fare = 2 * x[0] + 3 * x[1] + 4 * x[2]
    return fare

bnds = ((0, None), (0, None), (0, None))
x0 = [0, 0, 0]

res = minimize(fare_optimization, x0, bounds=bnds)
#StreamlitでWebアプリを作る
#最後に、Streamlitを使ってWebアプリを作成します。
#以下は、最適化問題を解くための入力フォームを作成し、結果を表示する例です。

import streamlit as st

st.title("Fare Optimization")

x0 = st.slider("Number of adult tickets", 0, 10, 0)
x1 = st.slider("Number of children tickets", 0, 10, 0)
x2 = st.slider("Number of senior tickets", 0, 10, 0)

if st.button("Optimize"):
    res = minimize(fare_optimization, [x0, x1, x2], bounds=bnds)
    st.success("Minimum fare: ${}".format(res.fun))
#上記のコードを実行し、Webブラウザでアクセスすることで、運賃の最小化問題を解くWebアプリが使用できます。




