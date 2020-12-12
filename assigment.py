import streamlit as st
import random
page_bg_img = '''
<style>
body {
#background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9_eXcz9ATGlyxvAs-3A-NT9SAB7g-qJ8Nsw&usqp=CAU");
background-image: url("https://miro.medium.com/max/2420/1*pzrQmqCuyNvpGSm0o3NEfQ.jpeg");
background-size: cover;
}
html = f"<a href='{https://miro.medium.com/max/2420/1*pzrQmqCuyNvpGSm0o3NEfQ.jpeg}'><img src='data:image/png;base64,{image_base64}'></a>"
st.markdown(html, unsafe_allow_html=True)
</style>
'''
from PIL import Image
image = Image.open('123456.jpg')

st.image(image, caption='UEFA Campion league', imgage_align='left', width="100", height="100" ,
         use_column_width=True)
st.markdown(page_bg_img, unsafe_allow_html=True)


#a=['Barcelona','Bayern','Benfica','Chelsea','Juventus','Paris','PSV','Zenit']
#b=['Arsenal','Astana','Atletico','Bate','CSKA Moskva','Dinamo Zagreb','Dynamo Kyiv','Galatasary','Gent','Leverkusen','Lyon','M. TEL','Malmo','Man. city','Man. United',
#   'Monchengladbach','olympiacosh','porto','Real Madrid','Romo','Sevilla','Shakhtar Donetsk','Valencia','Wolfsburg']
#c=['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F',' Group g','Group H' ]
#for i in range(0, 8):
 #  cols = st.beta_columns(5)
  # random.shuffle(b)
   #random.shuffle(a)
   #st.markdown("<h1 style='text-align: left; color: white;'>cols[0].write(f'{c[i]}')</h1>", unsafe_allow_html=True)
   #cols[0].write(f'{c[i]}')
   #cols[1].write(f'{a[0]}')
   #a.remove(a[0])
   #cols[2].write(f'{b[0]}')
   #b.remove(b[0])
   #cols[3].write(f'{b[0]}')
   #b.remove(b[0])
   #cols[4].write(f'{b[0]}')
   #b.remove(b[0])
   #cols[5].write('x' * i)




a=['Barcelona','Bayern','Benfica','Chelsea','Juventus','Paris','PSV','Zenit']
b=['Arsenal','Astana','Atletico','Bate','CSKA Moskva','Dinamo Zagreb','Dynamo Kyiv','Galatasary','Gent','Leverkusen','Lyon','M. TEL','Malmo','Man. city','Man. United',
   'Monchengladbach','olympiacosh','porto','Real Madrid','Romo','Sevilla','Shakhtar Donetsk','Valencia','Wolfsburg']
for i in range(0,1):
   cols = st.beta_columns(5)
   cols[1].header("Group A")
   cols[2].header("Group B")
   cols[3].header("Group C")
   cols[4].header("Group D")
for i in range(0,4):
   cols = st.beta_columns(5)
   random.shuffle(b)
   random.shuffle(a)
   cols[1].write(f'{a[0]}')
   a.remove(a[0])
   cols[2].write(f'{b[0]}')
   b.remove(b[0])
   cols[3].write(f'{b[0]}')
   b.remove(b[0])
   cols[4].write(f'{b[0]}')
   b.remove(b[0])


for i in range(0,1):
   cols = st.beta_columns(5)
   #cols[1].markdown("<h1 style='text-align: left; color: white;'>Group E</h1>", unsafe_allow_html=True)
   #cols[2].markdown("<h1 style='text-align: left; color: white;'>Group F</h1>", unsafe_allow_html=True)
   #cols[3].markdown("<h1 style='text-align: left; color: white;'>Group G</h1>", unsafe_allow_html=True)
   #cols[4].markdown("<h1 style='text-align: left; color: white;'>Group H</h1>", unsafe_allow_html=True)
   cols[1].header("Group E")
   cols[2].header("Group F")
   cols[3].header("Group G")
   cols[4].header("Group H")

for i in range(0,4):
   cols = st.beta_columns(5)
   random.shuffle(b)
   random.shuffle(a)
   cols[1].write(f'{a[0]}')
   a.remove(a[0])
   cols[2].write(f'{b[0]}')
   b.remove(b[0])
   cols[3].write(f'{b[0]}')
   b.remove(b[0])
   cols[4].write(f'{b[0]}')
   b.remove(b[0])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP A</h1>", unsafe_allow_html=True)
#st.title(a[0])
#st.title(b[0])
#st.title(b[1])
#st.title(b[2])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP B</h1>", unsafe_allow_html=True)
#st.title(a[1])
#st.title(b[3])
#st.title(b[4])
#st.title(b[5])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP C</h1>", unsafe_allow_html=True)
#st.title(a[2])
#st.title(b[6])
#st.title(b[7])
#st.title(b[8])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP D</h1>", unsafe_allow_html=True)
#st.title(a[3])
#st.title(b[9])
#st.title(b[10])
#st.title(b[11])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP E</h1>", unsafe_allow_html=True)
#st.title(a[4])
#st.title(b[12])
#st.title(b[13])
#st.title(b[14])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP F</h1>", unsafe_allow_html=True)
#st.title(a[5])
#st.title(b[15])
#st.title(b[16])
#st.title(b[17])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP G</h1>", unsafe_allow_html=True)
#st.title(a[6])
#st.title(b[18])
#st.title(b[19])
#st.title(b[20])
#st.markdown("<h1 style='text-align: left; color: white;'>GROUP H</h1>", unsafe_allow_html=True)
#st.title(a[7])
#st.title(b[21])
#st.title(b[22])
#st.title(b[23])

