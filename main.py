import time
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iteration.text(f'Itelation {i+1}')
   bar.progress( i+1 )
   time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
   right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は', 0,100,50)
#
# 'あなたの趣味:',  text
# 'コンディション:',  condition

# option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
# )
#
# 'あなたが好きな数字は',  option, 'です'

# if st.checkbox('Show Image'):
#    img = Image.open('Charlie.jpg')
#    st.image(img, caption='チャーリーじゃあーりませんか', use_column_width=True)

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=600, height=500)
# st.table(df.style.highlight_max(axis=0))


df = pd.DataFrame(
   np.random.rand(100, 2)/[50, 50] + [34.53, 135.48],
   columns=['lat', 'lon']
)

st.map(df)


# """
# 章
# # 節
# ## 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """