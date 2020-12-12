import streamlit as st
import random
page_bg_img = '''
<style>
body {
background-image: url("https://miro.medium.com/max/2420/1*pzrQmqCuyNvpGSm0o3NEfQ.jpeg");
background-size: cover;
}
</style>
'''







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
