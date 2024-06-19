import streamlit as st
st.header(":orange[**----💮----AREA VOLUME CALCULATOR----🌻----**]")


#) 2.chart with radiobutton
st.subheader("\n:violet[list of the shapes:🌞]\n")
RadioButton = st.radio('Select the chart: ',('cube',
                                             'cuboid'))
if RadioButton == 'cube':
    st.header(":green[1. cube🌨]")
    st.markdown("\n#### :red[1.1 the image of cube:🌳]\n")
    st.image("cube.png", caption='cube')
    #) user input for side measure of cube
    side_measure = st.number_input(":blue[Enter the value for side measure:]")
    if side_measure:
        #) lateral surface area
        st.markdown("\n#### :violet[1.1 lateral surface area of cube:👼]\n")
        lateral_surface_area = 4 *side_measure**2
        st.error(lateral_surface_area)
        st.write(":orange[----------------------------🌴--------------------------------------------------🍉--------------------------------]")
        
        #) total surface area
        st.markdown("\n#### :violet[1.2 total surface area of cube:🍯]\n")
        total_surface_area = 6*side_measure**2
        st.success(total_surface_area)
        st.write(":orange[-------------------------------☁-------------------------------------------------🍌------------------------------]")
        
        #)volume
        st.markdown("\n#### :violet[1.3 volume of cube:🗾]\n")
        volume = side_measure**3
        st.info(volume)
        st.write(":orange[----------------------------------🌚-----------------------------------------------🌩-----------------------------]")
    else:
         st.error("you have not entered the value of side measure🏒")

elif RadioButton == 'cuboid':
        st.header(":green[1. cube🌨]")
        st.markdown("\n#### :red[2.1 the image of cube:🌳]\n")
        st.image("cuboid.jpg", caption='cuboid')

        #) user input for l,b,h for cuboid
        length = st.number_input(":blue[Enter the value for length:]")
        if length:
             breadth = st.number_input(":blue[Enter the value for breadth:]")
             if breadth:
                  height = st.number_input(":blue[Enter the value for height:]")
                  if height:
                       #) lateral surface area
                       st.markdown("\n#### :violet[2.1 lateral surface area of cuboid:👼]\n")
                       lateral_surface_area = 2*(length + breadth)*height
                       st.error(lateral_surface_area)
                       st.write(":orange[----------------------------🌴--------------------------------------------------🍉--------------------------------]")
                       #) total surface area
                       st.markdown("\n#### :violet[2.2 total surface area of cube:🍯]\n")
                       total_surface_area = 2*((length*breadth) + (length*height) + (breadth*height))
                       st.success(total_surface_area)
                       st.write(":orange[-------------------------------☁-------------------------------------------------🍌------------------------------]")
                       #)volume
                       st.markdown("\n#### :violet[2.3 volume of cube:🗾]\n")
                       volume = length*breadth*height
                       st.info(volume)
                       st.write(":orange[----------------------------------🌚-----------------------------------------------🌩-----------------------------]")
                  else:
                        st.error("you havee not entered height value")
             else:
                  st.error("you have not entered breadth value 🏒")
        else:
             st.error("you not entered length value")
 
        
            