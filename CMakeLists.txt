cmake_minimum_required(VERSION 3.0.2)
project(action_template)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib_msgs
  smach_ros
  smach
  move_base_msgs
  message_generation
  jinko_service_msg
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
   add_rostest(test/test.test)
endif()

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
##add_service_files(
##  FILES emotionMessage.srv
##)

## Generate actions in the 'action' folder
add_action_files(
  DIRECTORY action
  FILES actionTemplate.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  
  actionlib_msgs
)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need

catkin_package(
  ##CATKIN_DEPENDS 
  ##rospy
  ##actionlib_msgs
  ##message_generation
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ${catkin_INCLUDE_DIRS}
)

 catkin_add_nosetests(test)